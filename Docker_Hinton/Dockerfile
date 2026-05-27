FROM nvidia/cuda:12.2.0-base-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3.10 python3-pip git build-essential \
    libssl-dev libffi-dev python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el archivo de requerimientos
COPY requirements.txt .

# 1. Instalamos PyTorch primero (es la base)
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# 2. Instalamos todo lo demás de tu lista (incluyendo transformers y gradio)
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gradio  # Lo añadimos por si no estaba en tu lista

COPY custom_welcome.py /usr/local/bin/welcome.py

EXPOSE 5050
EXPOSE 5051

CMD ["sh", "-c", "python3 /usr/local/bin/welcome.py || true && python3 /app/llm_hinton.py > /tmp/chatbot.log 2>&1 & jupyter lab --ip=0.0.0.0 --port=5050 --no-browser --allow-root --NotebookApp.token=''"]
