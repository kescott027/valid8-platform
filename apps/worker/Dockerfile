FROM python:3.11-slim

WORKDIR /app
RUN pip install uv

COPY pyproject.toml ./
RUN uv sync

COPY worker ./worker

ENV PYTHONUNBUFFERED=1
CMD ["uv", "run", "python", "-m", "worker"]
