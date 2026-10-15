ARG VARIANT="3.10"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}@sha256:ef9cc483a593c95e1e83f2cf00b6a0e1ec7df43344416a41ccb3a88aef27beac

USER vscode

COPY --from=ghcr.io/astral-sh/uv:0.13.0@sha256:cdc6093146eb3ff6a40107b38f008b789e050e77ad87865e381d9917da55a168 /uv /uvx /bin/

RUN echo "[[ -d .venv ]] && source .venv/bin/activate || export PATH=\$PATH" >> /home/vscode/.bashrc

HEALTHCHECK NONE
