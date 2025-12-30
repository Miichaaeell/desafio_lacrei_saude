FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "poetry==2.2.1"

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root

COPY . /app/

ENV PYTHONPATH="/app/src"

