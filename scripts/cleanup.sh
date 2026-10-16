# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

cleanup_paths=()
cleanup_pids=()
cleanup_worktrees=()
cleanup_repositories=()

cleanup_temp_dir() {
  local path
  path="$(mktemp -d "${TMPDIR:-/tmp}/$2.XXXXXX")" || return
  cleanup_paths+=("$path")
  printf -v "$1" '%s' "$path"
}

cleanup_worktree() {
  cleanup_repositories+=("$PWD")
  cleanup_worktrees+=("$1")
}

cleanup_track() {
  cleanup_pids+=("$1")
}

cleanup_wait() {
  local status=0 pid kept=()
  wait "$1" || status=$?
  for pid in ${cleanup_pids[@]+"${cleanup_pids[@]}"}; do
    [[ "$pid" == "$1" ]] || kept+=("$pid")
  done
  cleanup_pids=(${kept[@]+"${kept[@]}"})
  return "$status"
}

cleanup_wait_all() {
  local pid status=0
  for pid in ${cleanup_pids[@]+"${cleanup_pids[@]}"}; do
    cleanup_wait "$pid" || status=1
  done
  return "$status"
}

cleanup_descendants() {
  local child
  for child in $(pgrep -P "$1" || true); do
    printf '%s\n' "$child"
    cleanup_descendants "$child"
  done
}

cleanup_stop_children() {
  local pid child tries tree=()
  for pid in ${cleanup_pids[@]+"${cleanup_pids[@]}"}; do
    tree+=("$pid")
    while read -r child; do tree+=("$child"); done < <(cleanup_descendants "$pid")
  done
  ((${#tree[@]})) || return 0
  kill -TERM "${tree[@]}" 2>/dev/null || true
  for pid in "${cleanup_pids[@]}"; do wait "$pid" 2>/dev/null || true; done
  for pid in "${tree[@]}"; do
    for ((tries = 0; tries < 100; tries++)); do
      kill -0 "$pid" 2>/dev/null || break
      sleep 0.1
    done
    kill -0 "$pid" 2>/dev/null && kill -KILL "$pid" 2>/dev/null || true
  done
  cleanup_pids=()
}

cleanup_run() {
  local index path
  cleanup_stop_children
  for ((index = 0; index < ${#cleanup_worktrees[@]}; index++)); do
    git -C "${cleanup_repositories[index]}" worktree remove -f -f "${cleanup_worktrees[index]}" >/dev/null 2>&1 || true
  done
  for path in ${cleanup_paths[@]+"${cleanup_paths[@]}"}; do
    chmod -R u+w -- "$path" 2>/dev/null || true
    rm -rf -- "$path" || true
  done
}

cleanup_traps() {
  trap "${1:-cleanup_run}" EXIT
  trap 'exit 129' HUP
  trap 'exit 130' INT
  trap 'exit 143' TERM
}
