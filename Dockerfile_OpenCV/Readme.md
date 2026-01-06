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
1. Comandos para Abrir (Iniciar)
Existen dos formas dependiendo de si es la primera vez que lo lanzas o si el contenedor ya existe:

Primera vez (Crear y abrir): Usa el comando run con el mapeo de puertos y volúmenes.

Para OpenCV (Puerto 8889):


sudo docker run -p 8889:8888 -v "$(pwd)/Dockerfile_OpenCV:/app" opencv-jupyter:v1 

Para ML Principal (Puerto 8888):


sudo docker run -p 8888:8888 -v "$(pwd)/Dockerfile_MC:/app" ml-env:v1 

Si ya existe (Reiniciar): Si el contenedor está detenido pero no lo has borrado, búscalo con sudo docker ps -a y usa:


sudo docker start <ID_o_Nombre> 


2. Comandos para Cerrar (Detener)
Para cerrar el entorno de manera segura sin perder el trabajo sincronizado en tu carpeta local:

Desde la terminal donde corre: Presiona Ctrl + C dos veces. Esto enviará la señal de apagado al servidor de Jupyter.


Desde otra terminal (Recomendado):

Primero identifica el ID del contenedor: sudo docker ps.

Detén el proceso: sudo docker stop <ID_del_contenedor>.



Ejemplo de tu log: sudo docker stop practical_proskuriakova.