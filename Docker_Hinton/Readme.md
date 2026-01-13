
- http://localhost:5050: Sigue siendo tu base de operaciones. Aquí entras a JupyterLab, creas tus archivos .py y escribes tus notebooks.

- http://localhost:5051: Este será el enlace específico para la Interfaz de Chat (Gradio). Cuando ejecutes el script del modelo de lenguaje, la página con el fondo de los edificios cyberpunk y el chat neón se cargará en este puerto.

# 🤖 HINTON 1 - Neural Interface Control

Este proyecto despliega una interfaz de chat inteligente basada en **Llama-3.1** y **Gradio**, optimizada para ejecutarse en la GPU **NVIDIA RTX A6000** del Laboratorio FACI-UPCH.

## 🚀 Comandos de Gestión (Docker Compose)

Para gestionar el contenedor de la IA, abre una terminal en la carpeta del proyecto y utiliza:

1. Pausar el Servicio (Liberar GPU)
Si necesitas detener el procesamiento para que otro investigador use la RTX A6000:
sudo docker stop hinton_interactive_final

2. Reanudar el Servicio
Para volver a activar el chatbot sin perder la configuración del contenedor:
sudo docker start hinton_interactive_final

3. Ejecutar el Cerebro (Llama-3.1)
Una vez iniciado el contenedor, debes ejecutar el script para cargar el modelo en los 49GB de VRAM:
sudo docker exec -it hinton_interactive_final python3 /app/llm_hinton.py

4. Reinicio de Emergencia
Si el puerto 5051 deja de responder o la interfaz se congela:
sudo docker restart hinton_interactive_final