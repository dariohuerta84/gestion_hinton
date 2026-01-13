
- http://localhost:5050: Sigue siendo tu base de operaciones. Aquí entras a JupyterLab, creas tus archivos .py y escribes tus notebooks.

- http://localhost:5051: Este será el enlace específico para la Interfaz de Chat (Gradio). Cuando ejecutes el script del modelo de lenguaje, la página con el fondo de los edificios cyberpunk y el chat neón se cargará en este puerto.

# 🤖 HINTON 1 - Neural Interface Control

Este proyecto despliega una interfaz de chat inteligente basada en **Llama-3.1** y **Gradio**, optimizada para ejecutarse en la GPU **NVIDIA RTX A6000** del Laboratorio FACI-UPCH.

## 🚀 Comandos de Gestión (Docker Compose)

Para gestionar el contenedor de la IA, abre una terminal en la carpeta del proyecto y utiliza:

### 1. Iniciar el sistema
Levanta el contenedor en segundo plano (*detached mode*).
```bash
docker-compose up -d

### 2. Detener el sistema
Detiene los procesos pero mantiene el contenedor creado. Es útil para liberar RAM temporalmente.
docker-compose stop -d

### 3. Iniciar el sistema
Util para monitorear qué está pensando la IA o si hay errores de carga.
docker-compose logs -f

### 4. Ver logs en tiempo real
Util para monitorear qué está pensando la IA o si hay errores de carga.
docker-compose logs -f

### 5. Eliminar el contenedor
Detiene y borra el contenedor (pero no borra tu código ni tu imagen fondo.jpg).
docker-compose down

### 6. Reiniciar (Hard Reset)
Si el sistema se queda "congelado" o el puerto 5051 da error.
docker-compose restart