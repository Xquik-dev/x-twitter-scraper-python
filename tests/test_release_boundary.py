# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import json
import subprocess
from pathlib import Path

import pytest


def git(repository: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repository, capture_output=True, text=True, check=True)


@pytest.fixture
def release_repository(tmp_path: Path) -> Path:
    repository = tmp_path / "sdk"
    repository.mkdir()
    source = Path(__file__).parents[1]
    sources = (
        subprocess.run(["git", "ls-files", "-z", "--", "src"], cwd=source, capture_output=True, text=True, check=True)
        .stdout.rstrip("\0")
        .split("\0")
    )
    names = [
        "scripts/release",
        "scripts/check-all",
        "scripts/check-reproducible",
        "package.json",
        "pyproject.toml",
        "uv.lock",
        "README.md",
        "LICENSE",
        ".gitignore",
        *sources,
    ]
    for name in names:
        destination = repository / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes((source / name).read_bytes())
    git(repository, "init", "-q", "--initial-branch=main")
    git(repository, "config", "user.name", "Release test")
    git(repository, "config", "user.email", "release@example.test")
    git(repository, "config", "commit.gpgsign", "false")
    git(repository, "add", ".")
    git(repository, "commit", "-qm", "release fixture")
    return repository


def run_release(repository: Path, *args: str) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["UV_PUBLISH_TOKEN"] = "fixture-publisher-token"
    return subprocess.run(
        ["bash", str(repository / "scripts/release"), *args],
        cwd=repository,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )


@pytest.mark.parametrize("mode", ["prepare", "publish", "verify"])
def test_release_requires_clean_sources(release_repository: Path, mode: str) -> None:
    (release_repository / "untracked.py").write_text("value = 1\n")
    result = run_release(release_repository, mode)
    assert result.returncode == 1
    assert json.loads(result.stdout) == {"status": "failed", "exitCode": 1}
    assert "Commit verified changes" in result.stderr
    assert not (release_repository / "dist").exists()
    assert "fixture-publisher-token" not in result.stdout + result.stderr


def test_release_requires_a_supported_mode(release_repository: Path) -> None:
    result = run_release(release_repository, "invalid")
    assert result.returncode == 2
    assert json.loads(result.stdout) == {"status": "failed", "exitCode": 2}
    assert "Use prepare, publish, or verify." in result.stderr
    assert not (release_repository / "dist").exists()


def test_release_stops_when_native_checks_fail(release_repository: Path) -> None:
    result = run_release(release_repository, "prepare", "missing-coverage.json", "HEAD")
    assert result.returncode != 0
    assert json.loads(result.stdout)["status"] == "failed"
    assert "Parent coverage file is missing" in result.stderr
    assert not (release_repository / "dist").exists()


@pytest.mark.parametrize("tag", ["missing", "different revision"])
def test_publish_refuses_a_wrong_tag_before_preparing_artifacts(release_repository: Path, tag: str) -> None:
    if tag == "different revision":
        git(release_repository, "tag", "v0.12.0")
        git(release_repository, "commit", "--allow-empty", "-qm", "candidate")
    result = run_release(release_repository, "publish", "missing-coverage.json", "HEAD")
    assert result.returncode == 1
    assert json.loads(result.stdout) == {"status": "failed", "exitCode": 1}
    assert "The version tag must identify this release commit." in result.stderr
    assert not (release_repository / "dist").exists()


def test_publish_refuses_an_unmerged_commit_before_preparing_artifacts(
    release_repository: Path, tmp_path: Path
) -> None:
    origin = tmp_path / "origin.git"
    subprocess.run(["git", "init", "-q", "--bare", str(origin)], capture_output=True, text=True, check=True)
    git(release_repository, "remote", "add", "origin", str(origin))
    git(release_repository, "push", "-q", "origin", "HEAD:refs/heads/main")
    git(release_repository, "commit", "--allow-empty", "-qm", "unmerged candidate")
    git(release_repository, "tag", "v0.12.0")
    git(release_repository, "push", "-q", "origin", "refs/tags/v0.12.0")
    result = run_release(release_repository, "publish", "missing-coverage.json", "HEAD")
    assert result.returncode == 1
    assert json.loads(result.stdout) == {"status": "failed", "exitCode": 1}
    assert "Merge the release into main first." in result.stderr
    assert not (release_repository / "dist").exists()
