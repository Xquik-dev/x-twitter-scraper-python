# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import sys
import time
import signal
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
CHECK = r"""#!/usr/bin/env bash
name=$(basename "$0")
if [ "${1:-}" = --version ]; then [ "$CHECK_CASE" != no-codeql ] || exit 1; echo 2.27.2; exit; fi
printf '%s\n' "$name" >> "$CHECK_EVENTS"
case "$name" in
 test) printf '%s\n' '==> Running tests' '===== 3029 passed in 10.00s =====' '===== 3016 passed in 9.00s =====';;
 coverage-parent) printf 'report=%s\nrevision=%s\n' parent.json abc123 >> "$COVERAGE_PARENT_OUTPUT";;
 audit) [ "$CHECK_CASE" != changed ] || touch "$CHECK_DIRTY";;
esac
[ "$CHECK_CASE" != "$name" ]
"""
STUB = r"""git() {
 case "$1 $2" in
  'rev-parse --quiet') :;;
  'rev-parse HEAD') echo abc123;;
  'status --porcelain') if [ "$CHECK_CASE" = dirty ] || [ -e "$CHECK_DIRTY" ]; then echo ' M README.md'; fi;;
  *) exit 99;;
 esac
}
gh() {
 [ "$1 $2" = 'api --silent' ] || exit 99
 case "$3" in
  repos/Xquik-dev/x-twitter-scraper-python/commits/abc123) [ "$CHECK_CASE" != unpushed ];;
  repos/Xquik-dev/x-twitter-scraper-python/statuses/abc123)
   [ "$4 $6 $7 $8" = '-f -f context=xquik-local-checks -f' ] && [ "$#" = 9 ] || exit 99
   printf '%s: %s\n' "${5#state=}" "${9#description=}" >> "$CHECK_STATUSES";;
  *) exit 99;;
 esac
}
uv() {
 case "$1 $2" in
  'run --locked')
   case "$3 $4 $5 $6" in
    '--all-extras python -m scripts.check_api_coverage') printf 'api-coverage\n' >> "$CHECK_EVENTS"; [ "$CHECK_CASE" != api-coverage ];;
    '--all-extras python -m scripts.check_api_fields') printf 'api-fields\n' >> "$CHECK_EVENTS"; [ "$CHECK_CASE" != api-fields ];;
   esac;;
  'python find'|'sync --locked'|'build --out-dir') :;;
  'tool run') [ "$3 $4 $5 $6" = '--from reuse==6.2.0 reuse lint' ] || exit 99; printf 'reuse\n' >> "$CHECK_EVENTS";;
  *) exit 99;;
 esac
}
export -f git gh uv
runner=$1; shift
bash "$runner" "$@"
"""
CHECKS = [
    "api-coverage",
    "api-fields",
    "lint",
    "reuse",
    "check-reproducible",
    "test",
    "coverage-parent",
    "coverage",
    "audit",
    "codeql-security",
]
PENDING = "pending: Running API coverage & fields, lint, licensing, build, tests, coverage, audit & CodeQL."
PASSED = (
    "API coverage, API fields, lint & types, REUSE, reproducible build, metadata, 6045 tests in 2 runs, coverage, "
    "audit, CodeQL 2.27.2."
)


def run_checks(tmp_path: Path, case: str, *arguments: str) -> tuple[int, list[str], list[str], list[str]]:
    project = tmp_path / "project"
    for folder in ("bin", "scripts"):
        (project / folder).mkdir(parents=True)
    runner = project / "bin/check-local"
    runner.write_bytes((ROOT / "bin/check-local").read_bytes())
    (project / "scripts/cleanup.sh").write_bytes((ROOT / "scripts/cleanup.sh").read_bytes())
    for name in CHECKS:
        (project / "scripts" / name).write_text(CHECK)
    events, statuses = tmp_path / "events", tmp_path / "statuses"
    events.touch()
    statuses.touch()
    result = subprocess.run(
        ["bash", "-c", STUB, "check-local-test", str(runner), *arguments],
        env={
            **os.environ,
            "CHECK_CASE": case,
            "CHECK_EVENTS": str(events),
            "CHECK_STATUSES": str(statuses),
            "CHECK_DIRTY": str(tmp_path / "dirty"),
        },
        capture_output=True,
        text=True,
        check=False,
    )
    output = (result.stdout + result.stderr).splitlines()
    return result.returncode, events.read_text().splitlines(), statuses.read_text().splitlines(), output


def test_success_status_lists_the_checks_that_passed(tmp_path: Path) -> None:
    status, events, statuses, output = run_checks(tmp_path, "ready")
    assert status == 0, output
    assert events == CHECKS
    assert statuses == [PENDING, f"success: Passed {PASSED}"]
    assert output[-1] == f"All local checks passed. They were {PASSED}"


@pytest.mark.parametrize(
    "case,ran,failed",
    [
        ("api-coverage", CHECKS[:1], "API coverage: compare the SDK operations with the API spec"),
        ("api-fields", CHECKS[:2], "API fields: compare the SDK fields with the API spec"),
        ("lint", CHECKS[:3], "Lint: Ruff, Pyright, Mypy, and package import"),
        ("test", CHECKS[:6], "Tests: Python 3.10.22 and 3.14.8 with Pydantic 1 and 2"),
        ("audit", CHECKS[:9], "Dependency security: pip-audit and audit-exceptions.json"),
        ("codeql-security", CHECKS, "Static analysis: CodeQL 2.27.2 security-extended queries"),
        ("changed", CHECKS, "Final tree check"),
    ],
)
def test_failed_check_posts_failure_and_stops(tmp_path: Path, case: str, ran: list[str], failed: str) -> None:
    status, events, statuses, _ = run_checks(tmp_path, case)
    assert status != 0
    assert events == ran
    assert statuses == [PENDING, f"failure: Failed at {failed}."]


def test_unusable_codeql_fails_before_any_check(tmp_path: Path) -> None:
    status, events, statuses, _ = run_checks(tmp_path, "no-codeql")
    assert status == 1
    assert events == []
    assert statuses == [PENDING, "failure: Failed at CodeQL CLI."]


@pytest.mark.parametrize(
    "case,arguments,reason",
    [
        ("ready", ["--no-status"], "--no-status was passed."),
        ("dirty", [], "the tree has uncommitted changes."),
        ("unpushed", [], "GitHub does not have HEAD, or gh is signed out. Push first."),
    ],
)
def test_status_is_posted_only_for_a_clean_pushed_commit(
    tmp_path: Path, case: str, arguments: list[str], reason: str
) -> None:
    status, events, statuses, output = run_checks(tmp_path, case, *arguments)
    assert status == 0, output
    assert events == CHECKS
    assert statuses == []
    assert output[0] == f"==> Commit status not posted because {reason}"


CLEANUP_SCRIPTS: list[tuple[str, list[str]]] = [
    ("bin/check-local", ["--no-status", "HEAD"]),
    ("scripts/check-reproducible", []),
    ("scripts/licenses.sh", ["install"]),
    ("scripts/codeql-security", []),
    ("scripts/coverage-parent", ["HEAD"]),
    ("scripts/audit", []),
    ("scripts/fuzz", []),
    ("scripts/coverage", ["--baseline"]),
    ("scripts/check-all", ["parent.json"]),
    ("scripts/fuzz", ["remote"]),
]
CLEANUP_STEP = """import os, sys, time, signal
from pathlib import Path

paths = list(Path(os.environ["TMPDIR"]).iterdir())
assert paths
for path in paths:
    source = path / "source"
    readonly = (source if source.is_dir() else path) / f"readonly-{os.getpid()}"
    nested = readonly / "nested"
    nested.mkdir(parents=True)
    payload = nested / "payload"
    payload.write_text("fixture")
    payload.chmod(0o400)
    nested.chmod(0o500)
    readonly.chmod(0o500)
if "CLEANUP_STOPPED" in os.environ:
    def stopped(signum, frame):
        marker = Path(os.environ["CLEANUP_STOPPED"]) / str(os.getpid())
        marker.write_text(str(all(path.is_dir() for path in paths)))
        sys.exit(128 + signum)
    for signum in (signal.SIGHUP, signal.SIGINT, signal.SIGTERM):
        signal.signal(signum, stopped)
ready = Path(os.environ["CLEANUP_READY"])
ready.mkdir(exist_ok=True)
(ready / str(os.getpid())).touch()
if os.environ["CLEANUP_MODE"] == "fail":
    sys.exit(37)
time.sleep(60)
"""
CLEANUP_STUB = r"""cleanup_step() { "$CLEANUP_PYTHON" "$CLEANUP_STEP"; }
export -f cleanup_step
case "$CLEANUP_SCRIPT" in
 bin/check-local)
  uv() { cleanup_step; }
  export -f uv;;
 scripts/check-reproducible|scripts/audit|scripts/check-all)
  uv() { cleanup_step; }
  export -f uv;;
 scripts/licenses.sh)
  bun() { echo '0.1 fixture 1 0.1 1.0 fixture fixture'; }
  curl() { cleanup_step; }
  export -f bun curl;;
 scripts/coverage|scripts/coverage-parent)
  uv() {
   case " $* " in
    *' verify-parent '*) return 0;;
    *' snapshot '*) if [ "${CLEANUP_BACKGROUND:-}" = 1 ]; then return 0; fi;;
   esac
   cleanup_step
  }
  export -f uv;;
 scripts/fuzz)
  uname() { case "$1" in -s) echo Linux;; -m) echo x86_64;; *) return 99;; esac; }
  uv() { case " $* " in *' -c '*) echo "$CLEANUP_SANITIZER";; *) return 0;; esac; }
  systemd-run() { cleanup_step; }
  tar() { case "$1" in -xzf) cleanup_step;; *) printf fixture;; esac; }
  ssh() { [ "$1 $2" = '-- fixture' ] || return 99; printf '%s\n' "$3" | sh -n || return; bash -c "$3"; }
  export -f uname uv systemd-run tar ssh;;
esac
runner=$1; shift
exec bash "$runner" "$@"
"""


def cleanup_project(tmp_path: Path, script: str) -> tuple[Path, dict[str, str]]:
    project = tmp_path / "project"
    for folder in ("bin", "scripts"):
        (project / folder).mkdir(parents=True)
    for name in (script, "scripts/cleanup.sh"):
        (project / name).write_bytes((ROOT / name).read_bytes())
    subprocess.run(["git", "init", "--quiet", str(project)], check=True, capture_output=True)
    common = subprocess.run(
        ["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()
    (project / ".git/objects/info/alternates").write_text(f"{common}/objects\n")
    (project / ".git/HEAD").write_text(f"{revision}\n")
    (project / "parent.json").write_text("{}")
    if script == "scripts/fuzz":
        (project / "scripts/audit").write_text("exit 0\n")
    if script == "bin/check-local":
        (project / "scripts/codeql-security").write_text("cleanup_step\n")
    codeql = tmp_path / "codeql"
    codeql.write_text('#!/usr/bin/env bash\nif [ "$1" = version ]; then echo 2.27.2; else cleanup_step; fi\n')
    codeql.chmod(0o755)
    sanitizer = tmp_path / "sanitizer.so"
    sanitizer.touch()
    step = tmp_path / "step.py"
    step.write_text(CLEANUP_STEP)
    temporary = tmp_path / "temporary"
    temporary.mkdir()
    return project, {
        **os.environ,
        "TMPDIR": str(temporary),
        "CLEANUP_SCRIPT": script,
        "CLEANUP_PYTHON": sys.executable,
        "CLEANUP_STEP": str(step),
        "CLEANUP_READY": str(tmp_path / "ready"),
        "CLEANUP_SANITIZER": str(sanitizer),
        "XQUIK_CODEQL_BIN": str(codeql),
        "XQUIK_FUZZ_HOST": "",
    }


def worktrees(project: Path) -> str:
    return subprocess.run(
        ["git", "worktree", "list", "--porcelain"],
        cwd=project,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def run_cleanup(
    project: Path,
    environment: dict[str, str],
    arguments: list[str],
    stop: signal.Signals | None,
    *,
    command: str = CLEANUP_STUB,
) -> subprocess.CompletedProcess[str]:
    ready = Path(environment["CLEANUP_READY"])
    environment["CLEANUP_MODE"] = "fail" if stop is None else "signal"
    if arguments == ["remote"]:
        arguments = []
        environment["XQUIK_FUZZ_HOST"] = "fixture"
    process = subprocess.Popen(
        ["bash", "-c", command, "cleanup-test", str(project / environment["CLEANUP_SCRIPT"]), *arguments],
        cwd=project,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=True,
    )
    try:
        if stop is not None:
            deadline = time.monotonic() + 10
            expected = int(environment.get("CLEANUP_READY_COUNT", "1"))
            while process.poll() is None and time.monotonic() < deadline:
                if ready.is_dir() and len(list(ready.iterdir())) == expected:
                    break
                time.sleep(0.01)
            assert ready.exists(), process.communicate(timeout=10)
            assert len(list(ready.iterdir())) == expected
            os.killpg(process.pid, stop)
        stdout, stderr = process.communicate(timeout=15)
    finally:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.communicate(timeout=10)
    assert ready.exists(), stdout + stderr
    return subprocess.CompletedProcess(process.args, process.returncode, stdout, stderr)


@pytest.mark.parametrize("script,arguments", CLEANUP_SCRIPTS)
@pytest.mark.parametrize(
    "stop,status", [(None, 37), (signal.SIGHUP, 129), (signal.SIGINT, -signal.SIGINT), (signal.SIGTERM, 143)]
)
def test_scripts_remove_readonly_temporary_directories_on_failure_or_signal(
    tmp_path: Path, script: str, arguments: list[str], stop: signal.Signals | None, status: int
) -> None:
    project, environment = cleanup_project(tmp_path, script)
    registered = worktrees(project)
    result = run_cleanup(project, environment, arguments, stop)
    assert result.returncode == status, result.stdout + result.stderr
    assert list(Path(environment["TMPDIR"]).iterdir()) == []
    assert worktrees(project) == registered


@pytest.mark.parametrize("script", ["scripts/coverage", "scripts/coverage-parent"])
@pytest.mark.parametrize("stop,status", [(signal.SIGHUP, 129), (signal.SIGINT, -signal.SIGINT), (signal.SIGTERM, 143)])
def test_coverage_stops_background_children_before_removing_their_directories(
    tmp_path: Path, script: str, stop: signal.Signals, status: int
) -> None:
    project, environment = cleanup_project(tmp_path, script)
    registered = worktrees(project)
    stopped = tmp_path / "stopped"
    stopped.mkdir()
    environment.update(CLEANUP_BACKGROUND="1", CLEANUP_READY_COUNT="3", CLEANUP_STOPPED=str(stopped))
    arguments = ["--baseline"] if script == "scripts/coverage" else ["HEAD"]
    result = run_cleanup(project, environment, arguments, stop)
    assert result.returncode == status, result.stdout + result.stderr
    assert len(list(stopped.iterdir())) == 3
    assert all(marker.read_text() == "True" for marker in stopped.iterdir())
    assert list(Path(environment["TMPDIR"]).iterdir()) == []
    assert worktrees(project) == registered


def test_sigint_stops_a_parent_without_an_int_trap_before_its_next_command(tmp_path: Path) -> None:
    project, environment = cleanup_project(tmp_path, "scripts/check-reproducible")
    continued = tmp_path / "continued"
    environment.update(CLEANUP_COMMAND=CLEANUP_STUB, CLEANUP_CONTINUED=str(continued))
    result = run_cleanup(
        project,
        environment,
        [],
        signal.SIGINT,
        command='bash -c "$CLEANUP_COMMAND" cleanup-test "$@"\ntouch "$CLEANUP_CONTINUED"',
    )
    assert result.returncode == -signal.SIGINT, result.stdout + result.stderr
    assert not continued.exists()
    assert list(Path(environment["TMPDIR"]).iterdir()) == []


def test_cleanup_kills_and_reaps_a_tracked_child_that_ignores_sigterm(tmp_path: Path) -> None:
    project, environment = cleanup_project(tmp_path, "scripts/check-reproducible")
    result = run_cleanup(
        project,
        environment,
        [],
        signal.SIGTERM,
        command="""source scripts/cleanup.sh
cleanup_traps
cleanup_temp_dir evidence xquik-python-cleanup
(
  trap '' TERM
  exec "$CLEANUP_PYTHON" "$CLEANUP_STEP"
) &
cleanup_track "$!"
cleanup_wait "$!"
""",
    )
    assert result.returncode == 143, result.stdout + result.stderr
    assert list(Path(environment["TMPDIR"]).iterdir()) == []
    for child in Path(environment["CLEANUP_READY"]).iterdir():
        with pytest.raises(ProcessLookupError):
            os.kill(int(child.name), 0)


def test_coverage_does_not_resolve_a_baseline_when_comparing_parent_coverage(tmp_path: Path) -> None:
    project, environment = cleanup_project(tmp_path, "scripts/coverage")
    environment["BASH_ENV"] = str(tmp_path / "bash-env")
    Path(environment["BASH_ENV"]).write_text("git() { return 99; }\nexport -f git\n")
    result = run_cleanup(project, environment, ["parent.json", "HEAD"], None)
    assert result.returncode == 37, result.stdout + result.stderr
    assert list(Path(environment["TMPDIR"]).iterdir()) == []


@pytest.mark.parametrize(
    "script,arguments,report,relative",
    [
        ("scripts/coverage", ["--baseline"], "xquik-coverage-baseline.json", False),
        ("scripts/coverage-parent", ["HEAD"], "xquik-parent-coverage.json", False),
        ("scripts/coverage-parent", ["HEAD"], "parent.json", True),
    ],
)
def test_coverage_keeps_successful_reports_after_temporary_directories_are_removed(
    tmp_path: Path, script: str, arguments: list[str], report: str, relative: bool
) -> None:
    project, environment = cleanup_project(tmp_path, script)
    registered = worktrees(project)
    environment.update(
        COVERAGE_BASELINE="", COVERAGE_PARENT_REPORT=report if relative else "", BASH_ENV=str(tmp_path / "bash-env")
    )
    Path(environment["BASH_ENV"]).write_text(
        """uv() {
 while (($#)); do
  case "$1" in -o) printf '{"fixture":true}\\n' > "$2"; return;; esac
  shift
 done
}
export -f uv
"""
    )
    result = subprocess.run(
        ["bash", str(project / script), *arguments],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert list(Path(environment["TMPDIR"]).iterdir()) == []
    assert worktrees(project) == registered
    destination = tmp_path / report if relative else project / ".git" / report
    assert destination.read_text() == '{"fixture":true}\n'
    assert str(destination) in result.stdout
