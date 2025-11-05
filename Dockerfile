FROM python:3.10-slim

WORKDIR /app

COPY dockerfile/ /app/

CMD ["python", "app.py"]

