# Docker_Hinton — HINTON 1 (Interfaz Neural)

> Repositorio para ejecutar JupyterLab y un chatbot Gradio acelerado por GPU NVIDIA.

## Resumen

- **JupyterLab** (IDE / Notebooks) → puerto `5050`
- **Chatbot (Gradio)** → puerto `5051` (usa GPU)

## Estructura principal

```
Docker_Hinton/
├── Dockerfile
├── docker-compose.yml
├── llm_hinton.py         # Script principal del chatbot (Gradio)
├── custom_welcome.py     # Mensaje de bienvenida al iniciar el contenedor
├── requirements.txt
└── app/
    ├── main_notebook.ipynb
    ├── Untitled.ipynb
    └── fondo.jpg         # Imagen usada como fondo por la UI
```

## Requisitos

- Docker
- NVIDIA drivers (host) y `nvidia-container-toolkit` o `nvidia-docker2`
- Docker Compose v2 (`docker compose`)
- Conexión a Internet para descargar pesos del modelo en la primera ejecución

> Nota: el modelo puede requerir mucha VRAM (recomendado ≥ 16 GB; 48 GB ideal para modelos grandes).

## Despliegue en otra máquina (paso a paso)

1. Clona o copia el repositorio en la máquina destino:

```bash
git clone https://github.com/dariohuerta84/gestion_hinton.git
cd gestion_hinton/Docker_Hinton
```

2. (Opcional) Configura usuario para usar Docker sin `sudo`:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

3. (Opcional) Si alguna herramienta busca el socket en la ruta de Docker Desktop:

```bash
sudo mkdir -p ~/.docker/desktop
sudo ln -sf /var/run/docker.sock ~/.docker/desktop/docker.sock
```

4. Construcción (opcional — `docker compose` construye si falta):

```bash
docker build -t hinton-ultimate .
```

5. Levantar los servicios:

```bash
docker compose up -d
```

6. Verificar:

```bash
docker ps
# ver logs
docker logs -f hinton_interactive_final
```

## Acceso

- JupyterLab: http://localhost:5050/lab
- Chatbot (Gradio): http://localhost:5051

## Comandos útiles

- Levantar (foreground): `docker compose up`
- Levantar (background): `docker compose up -d`
- Parar (liberar GPU): `docker compose stop` o `docker stop hinton_interactive_final`
- Iniciar: `docker compose start` o `docker start hinton_interactive_final`
- Reiniciar: `docker compose restart` o `docker restart hinton_interactive_final`
- Borrar: `docker compose down`
- Reconstruir imagen: `docker build -t hinton-ultimate .`
- Ejecutar chatbot manualmente dentro del contenedor:
  `docker exec -it hinton_interactive_final python3 /app/llm_hinton.py`

## Variables y recomendaciones

- Si usas Hugging Face y quieres evitar límites anónimos, exporta tu token:

```bash
export HF_TOKEN="<tu_token>"
```

- La primera ejecución descarga varios GB; sé paciente.
- Si el contenedor no ve la GPU, comprueba `nvidia-smi` en el host y que `nvidia-container-toolkit` esté instalado.

## Solución rápida de problemas

- `Cannot connect to the Docker daemon`: arranca `dockerd` y añade el usuario al grupo `docker`.
- `Error pull access denied for hinton-ultimate`: ejecuta `docker build -t hinton-ultimate .` en la carpeta del Dockerfile.
- `Puerto 5051 no disponible`: revisa `docker logs hinton_interactive_final` y `/tmp/chatbot.log` dentro del contenedor.
- `fondo.jpg not found`: asegúrate que `app/fondo.jpg` existe y que `docker-compose.yml` monta el volumen (por defecto `.:/app`).

## Notas finales

1. Ambos servicios corren dentro del mismo contenedor y se exponen en puertos distintos.
2. Si prefieres separar Jupyter y Gradio en servicios/containers distintos, puedo actualizar `docker-compose.yml` para eso.



Docker Compose
└── chatbot-hinton (container: hinton_interactive_final)
    ├── Volumen: .:/app
    ├── GPU: runtime nvidia
    ├── Puertos:
    │   ├── 5051 → Gradio chatbot
    │   └── 5050 → JupyterLab
    ├── Entorno:
    │   ├── NVIDIA_VISIBLE_DEVICES=all
    │   ├── NVIDIA_DRIVER_CAPABILITIES=compute,utility
    │   └── HF_TOKEN=${HF_TOKEN}
    └── Código principal:
        └── /app/llm_hinton.py
            ├── Carga modelo Hugging Face
            │   ├── unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit
            │   ├── dtype=torch.bfloat16
            │   └── device_map="auto"
            ├── Autenticación:
            │   └── use_auth_token = HF_TOKEN
            ├── Prompt del sistema:
            │   └── HINTON_KNOWLEDGE
            │       ├── HINTON 1 info
            │       ├── HINTON 2 info
            │       ├── manual/reglamento
            │       └── creador: Matias Dario Huerta Cruz
            ├── Función de chat:
            │   └── chat_func(message, history)
            │       ├── role: system → HINTON_KNOWLEDGE
            │       └── role: user → message
            └── Interfaz Gradio:
                ├── gr.Blocks
                ├── gr.HTML(title)
                ├── gr.ChatInterface(fn=chat_func)
                └── CSS:
                    ├── fondo blanco
                    ├── logo centered: logoupch.jpg
                    └── panel de chat semi-transparente
..