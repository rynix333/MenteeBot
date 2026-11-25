FROM python:3.12-slim AS runtime
ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION} PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
LABEL org.opencontainers.image.version=${APP_VERSION}
WORKDIR /app
RUN useradd -r -u 10001 app
COPY --chown=app hello_world.py .
USER app
EXPOSE 8080
HEALTHCHECK CMD python -c "import urllib.request as u; u.urlopen('http://localhost:8080/healthz')"
CMD ["python", "hello_world.py"]