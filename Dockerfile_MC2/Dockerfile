FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

# Dependencias de sistema para PyTorch y numpy
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

CMD ["python", "app/main.py"]
