FROM ghcr.io/astral-sh/uv:0.11.6@sha256:b1e699368d24c57cda93c338a57a8c5a119009ba809305cc8e86986d4a006754 AS uv

FROM gcr.io/oss-fuzz-base/base-builder-python@sha256:bb1b8ebd512e29bc955d2ef4de4b141b38809249cc66ff2fd2947dfcb6a9b012

COPY --from=uv /uv /uvx /bin/
COPY . $SRC/x-twitter-scraper-python

WORKDIR $SRC/x-twitter-scraper-python

RUN uv export \
      --locked \
      --no-dev \
      --no-emit-project \
      --format requirements-txt \
      --output-file /tmp/fuzz-requirements.txt \
    && uv pip install \
      --system \
      --require-hashes \
      --requirement /tmp/fuzz-requirements.txt \
    && rm /tmp/fuzz-requirements.txt

COPY .clusterfuzzlite/build.sh $SRC/
