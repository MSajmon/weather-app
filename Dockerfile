FROM python:3.12-slim AS builder
LABEL org.opencontainers.image.authors="Szymon Marczak"

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=5000
EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3  CMD curl --fail http://localhost:5000 || exit 1

CMD ["python", "app.py"]