# Aca comenzaremos con la instalacion, para lo que necesitaremops instalar panda y numpys scikit-learn, incluso tensorflow o pytorch

## Imagen base ligera de Python
FROM python:3.10-slim

## Establecer el directorio de trabajo
WORKDIR /app

## Copiar los archivos del proyecto
COPY . /app

## Instalar dependencias del sistema (por si algunas libs lo necesitan)
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

## Instalar librerías de Machine Learning
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    scikit-learn \
    matplotlib \
    seaborn \
    jupyter

## Si quieres usar TensorFlow o PyTorch (opcional):
RUN pip install tensorflow
RUN pip install torch torchvision torchaudio

## Exponer el puerto de Jupyter Notebook
EXPOSE 8888

## Comando por defecto (inicia Jupyter Notebook)
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]