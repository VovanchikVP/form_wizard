FROM kapitonovvp/ubuntu_uv_ffmpeg AS base

WORKDIR /opt/app-root/
COPY src src/
COPY data data/
COPY .python-version .
COPY pyproject.toml .

ENV PATH="/root/.local/bin/:$PATH"
ENV PYTHONPATH=.

RUN uv sync

ENV TZ="Europe/Moscow"

FROM base AS master

CMD uv run src/main.py
