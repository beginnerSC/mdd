# Use official Python runtime as base image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy pyproject.toml and poetry.lock (if it exists)
COPY pyproject.toml poetry.lock* .

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

# Copy application code
COPY mdd/ ./mdd/

# Expose port
EXPOSE 8050

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8050/').read()" || exit 1

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "--workers", "1", "--threads", "2", "--worker-class", "gthread", "mdd.app:server"]
