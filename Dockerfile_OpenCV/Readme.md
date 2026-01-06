# OpenCV + Jupyter Interactive Environment

[cite_start]Este entorno proporciona una plataforma de desarrollo especializada en **Visión Computacional**, integrando la potencia de **OpenCV** con la interactividad de **Jupyter Notebook** [cite: 610-612]. Está diseñado para realizar pre-procesamiento de imágenes, detección de características y visualización de datos visuales en tiempo real de forma persistente.

## 📋 1. Funciones del Entorno
* **Procesamiento de Imágenes:** Manipulación de matrices de píxeles mediante OpenCV y NumPy.
* **Desarrollo Interactivo:** Visualización inmediata de filtros y transformaciones usando la interfaz web de Jupyter en el puerto 8888.
* **Soporte Gráfico:** Incluye dependencias de sistema críticas (`libgl1`, `libglib2.0`, etc.) necesarias para el renderizado de imágenes en contenedores Linux "slim".
* [cite_start]**Persistencia de Datos:** Sincronización bidireccional de archivos entre el host y el contenedor mediante montajes de volumen (`-v`) [cite: 663-664].

## 🛠️ Tecnologías Principales
* **Base Image:** `python:3.10-slim`.
* **Framework:** `opencv-python` (Visión artificial).
* **Interfaz:** `jupyter` (Notebooks interactivos).
* **Visualización:** `matplotlib` y `seaborn`.
* **Cálculo:** `numpy`.

## 🚀 2. Guía de Ejecución (Paso a Paso)

### Construcción de la Imagen
Desde la raíz del repositorio (`gestion_hinton`), ejecuta el comando de construcción especificando el contexto de la carpeta:
```bash
sudo docker build -t opencv-jupyter:v1 -f Dockerfile_OpenCV/Dockerfile Dockerfile_OpenCV

### Lanzamiento del Contenedor
Inicia el entorno mapeando el puerto a uno libre (ej. 8889) para evitar conflictos con otros contenedores activos como Dockerfile_MC: