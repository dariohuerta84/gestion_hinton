# Limited + Jupyter Environment

Este entorno proporciona un laboratorio interactivo ligero diseñado para pruebas rápidas de datos y manipulación de estructuras básicas dentro del repositorio **gestion_hinton**. Se ha transformado de un servidor estático Nginx a un entorno de **Jupyter Notebook**.

## 📋 1. Funciones del Entorno
* **Laboratorio Ligero:** Optimizado para ejecutar scripts que no requieren las librerías pesadas de los entornos de ML o Visión.
* **Interfaz Interactiva:** Proporciona una plataforma web para programar en Python en tiempo real.
* **Persistencia de Datos:** Sincronización automática entre la carpeta local `Dockerfile_Limited/` y el directorio `/app` del contenedor.

## 🛠️ Tecnologías Principales
* **Base:** Python 3.10-slim.
* **Librerías instaladas:** `jupyter`, `numpy`, `pandas`.

## 🚀 2. Guía de Gestión (Ciclo de Vida)

### Iniciar por primera vez (Build + Run)
Desde la raíz del repositorio (`gestion_hinton`), ejecuta:

```bash
# 1. Construir la imagen localmente
sudo docker build -t limited-jupyter:v1 -f Dockerfile_Limited/dockerfile Dockerfile_Limited

# 2. Crear y lanzar el contenedor en el puerto 8890
sudo docker run -p 8890:8888 -v "$(pwd)/Dockerfile_Limited:/app" limited-jupyter:v1
Cerrar el entorno (Detener)
Para apagar el servidor de Jupyter de forma segura:

Desde la terminal activa: Presiona Ctrl + C dos veces seguidas.

Desde otra terminal (Forzado):

bash
Copy code
# Buscar el ID del contenedor
sudo docker ps
# Detenerlo
sudo docker stop <ID_DEL_CONTENEDOR>
Reiniciar el entorno (Start)
Si el contenedor ya fue creado anteriormente y solo deseas encenderlo de nuevo:

bash
Copy code
sudo docker start <ID_O_NOMBRE_DEL_CONTENEDOR>
🌐 3. Acceso al Servidor

Localizar el Token: Busca en la terminal la línea que indica el token de seguridad.

URL de acceso: Ingresa en el navegador a: http://localhost:8890/?token=COPIAR_TOKEN_AQUI.

Puerto asignado: 8890


