# Base con drivers de NVIDIA para Ubuntu
FROM nvidia/cuda:12.2.0-base-ubuntu22.04 [cite: 331]     # Aplicacion de Cuda de NVIDIA para aprovechar la GPU del host

# Evitar diálogos interactivos durante la instalación
ENV DEBIAN_FRONTEND=noninteractive [cite: 611]

# Instalación de dependencias de sistema y gráficas (X11 y OpenGL)
# Crucial para que el emulador "dibuje" en la pantalla del host
RUN apt-get update && apt-get install -y \
    software-properties-common \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxext6 \
    libxrender1 \
    libsm6 \
    build-essential \
    && add-apt-repository ppa:gregory-hainaut/pcsx2.official.ppa \
    && apt-get update && apt-get install -y pcsx2-unstable \
    && rm -rf /var/lib/apt/lists/* [cite: 593, 596, 601]

# Directorio de trabajo interno
WORKDIR /app [cite: 614]

# Exponer el puerto en caso de usar acceso remoto via VNC/Web
EXPOSE 8888 [cite: 625]

# El comando de inicio lanza el emulador
CMD ["pcsx2"] [cite: 627]