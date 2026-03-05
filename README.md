# Gestión de Infraestructura Hinton 1 & 2

Administración de entornos de **Machine Learning, visión computacional y experimentación** utilizando **Docker** en los servidores **HINTON 1** y **HINTON 2** del laboratorio **GESTIÓN HINTON**.

Este repositorio documenta:

- despliegue de contenedores Docker
- gestión de entornos de Machine Learning
- uso de Jupyter en contenedores
- administración de sesiones persistentes con `tmux`
- comandos de operación del sistema

El objetivo es mantener **entornos reproducibles, aislados y administrables** para investigación y experimentación en IA.

---

# Arquitectura del repositorio

```
gestion_hinton
│
├── Dockerfile
│
├── Dockerfile_MC
│   └── entorno Deep Learning con Jupyter
│
├── Dockerfile_MC2
│   └── pipeline de entrenamiento ML con PyTorch
│
├── Dockerfile_OpenCV
│   └── entorno de visión computacional
│
├── Dockerfile_Sklearn
│   └── entorno de experimentación ML
│
├── Dockerfile_Limited
│   └── entorno Jupyter liviano
│
└── README.md
```

---

# Resumen de Trabajo

## Sesión — 12 de noviembre (11:36)

El contenedor Docker se ejecutó correctamente con **Jupyter Notebook**.

Se montó la carpeta local:

```
Dockerfile_MC
```

Esto permitió sincronizar los cambios entre el host y el contenedor.

Beneficios obtenidos:

- acceso a archivos desde el navegador
- persistencia del código en el host
- entorno reproducible

### Comandos utilizados

Detener contenedor:

```bash
sudo docker stop practical_proskuriakova
```

Reiniciar contenedor:

```bash
sudo docker start practical_proskuriakova
```

Visualizar imágenes Docker:

```bash
sudo docker images
```

Visualizar contenedores activos:

```bash
sudo docker ps
```

---

# Gestión de Branches

Actualizar referencias remotas sin mezclar cambios:

```bash
git fetch --all
```

Cambiar a rama principal:

```bash
git checkout main
```

Sobrescribir rama remota con versión local:

```bash
git push origin main --force
```

---

# Sesión — 17 de noviembre (11:46)

## Configuración de entorno Machine Learning

Se configuró un entorno de **Machine Learning reproducible dentro de Docker** utilizando **PyTorch**.

### Framework seleccionado

```
torch==2.2.0
```

Se eligió **PyTorch CPU-only** debido a:

- menor peso del contenedor
- simplicidad para experimentación
- no requerir GPU
- rapidez de despliegue

---

# Estructura del entorno ML

Directorio utilizado:

```
Dockerfile_MC2
```

Estructura:

```
Dockerfile_MC2
│
├── Dockerfile
├── requirements.txt
└── app
    └── main.py
```

---

# Dependencias

Archivo `requirements.txt`

```txt
numpy
torch==2.2.0
```

El objetivo fue mantener un contenedor **ligero y rápido de construir**.

---

# Script de validación del entorno

El archivo:

```
app/main.py
```

verifica el funcionamiento del entorno mediante:

1. generación de datos sintéticos

```
y = 3x + 2
```

2. construcción de una red neuronal multicapa (MLP)

3. entrenamiento durante múltiples épocas

4. impresión de la pérdida (`loss`)

5. predicción final del modelo

---

# Imagen base del contenedor

Se utilizó:

```
python:3.10-slim
```

Esto permite:

- menor tamaño de imagen
- menor tiempo de construcción
- menor consumo de recursos

El contenedor ejecuta automáticamente:

```bash
python app/main.py
```

---

# Almacenamiento Docker

Las imágenes Docker se almacenan en:

```
/var/lib/docker
```

Para listarlas:

```bash
sudo docker images
```

---

# Uso de Scikit-learn

**Scikit-learn** es una biblioteca de Python especializada en **Machine Learning clásico**.

Permite implementar algoritmos de:

- clasificación
- regresión
- clustering
- reducción de dimensionalidad
- validación de modelos

Es ampliamente utilizada para **prototipado rápido y pruebas de modelos**.

---

# Administración de usuarios en Hinton

Se comenzó la gestión de uso de recursos en los servidores:

- HINTON 1
- HINTON 2

Herramientas utilizadas:

- Linux
- Docker
- tmux
- SSH

---

# Comandos Docker utilizados

Listar todos los contenedores:

```bash
sudo docker ps -a
```

Detener contenedor:

```bash
sudo docker stop ID
```

Iniciar contenedor:

```bash
sudo docker start ID
```

Eliminar contenedor detenido:

```bash
sudo docker rm ID
```

Forzar eliminación:

```bash
sudo docker rm -f NOMBRE
```

---

# Conexión entre servidores

Acceso por SSH:

```bash
ssh hinton2@Direccion_IP
```

---

# Uso de tmux

`tmux` permite mantener procesos ejecutándose incluso si se pierde la conexión SSH.

Listar sesiones activas:

```bash
tmux ls
```

Crear sesión:

```bash
tmux new -s nombre_sesion
```

Adjuntarse a sesión existente:

```bash
tmux attach -t nombre_sesion
```

Desconectarse sin detener procesos:

```
Ctrl + b  luego  d
```

Eliminar sesión:

```bash
tmux kill-session -t nombre_sesion
```

---

# Contenedores disponibles

| Docker | Función | Puerto | Jupyter |
|------|------|------|------|
| DockerFile | Test básico | N/A | No |
| DockerFile_MC | Deep Learning | 8888 | Sí |
| DockerFile_MC2 | Pipeline ML | N/A | No |
| docker_opencv | Visión computacional | 8889 | Sí |
| DockerFile_Sklearn | ML experimental | 5000 | No |
| docker_limited | Jupyter liviano | 8890 | Sí |

---

# Ejecución de contenedores

### Deep Learning Stack

```bash
sudo docker build -t dockerfile_mc -f Dockerfile_MC/Dockerfile Dockerfile_MC

sudo docker rm -f docker_mc || true

sudo docker run -d \
--name docker_mc \
-p 8888:8888 \
-v /home/hinton1/Documents/ADMINISTRACION/repo/gestion_hinton/Dockerfile_MC:/app \
dockerfile_mc
```

---

### Pipeline ML

```bash
sudo docker build -t dockerfile_mc2 -f Dockerfile_MC2/Dockerfile Dockerfile_MC2

sudo docker run --rm \
--name docker_mc2_pipeline \
-v /home/hinton1/Documents/ADMINISTRACION/repo/gestion_hinton/Dockerfile_MC2:/app \
dockerfile_mc2
```

---

# Roadmap

Próximas mejoras del sistema:

- publicación de imágenes en **DockerHub**
- integración de análisis con **DeepWiki**
- exploración de **Nested Learning**
- investigación sobre infraestructura **Radware**

---

# Futuro contenedor: Docker_Hinton

Se plantea desarrollar un contenedor optimizado denominado:

```
Docker_Hinton
```

Objetivo:

Aprovechar completamente el hardware del servidor **HINTON 1**.

Características previstas:

- optimización para entrenamiento de modelos
- soporte para aceleración por hardware
- mejor gestión de memoria
- compatibilidad con GPU (CUDA)
- librerías optimizadas de ML y DL

Este contenedor servirá como **base para entrenamiento de modelos más complejos**.
