#!/bin/bash -eu

# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

export PYTHONPATH="$SRC/x-twitter-scraper-python/src"

compile_python_fuzzer \
  "$SRC/x-twitter-scraper-python/.clusterfuzzlite/fuzz_querystring.py" \
  --hidden-import atheris

cat > "$OUT/fuzz_querystring.options" <<'EOF'
[libfuzzer]
max_len = 4096
EOF
