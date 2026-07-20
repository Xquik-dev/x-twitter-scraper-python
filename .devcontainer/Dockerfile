ARG VARIANT="3.10"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}@sha256:ef9cc483a593c95e1e83f2cf00b6a0e1ec7df43344416a41ccb3a88aef27beac

USER vscode

COPY --from=ghcr.io/astral-sh/uv:latest@sha256:93b61e21202b1dab861092748e46bbd6e0e41dd84f59b9174efd2353186e1b47 /uv /uvx /bin/

RUN echo "[[ -d .venv ]] && source .venv/bin/activate || export PATH=\$PATH" >> /home/vscode/.bashrc
