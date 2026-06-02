import gradio as gr
import torch
from transformers import pipeline
import base64
import os

# 1. IA Core
model_id = "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit"
pipe = pipeline("text-generation", model=model_id, model_kwargs={"dtype": torch.bfloat16}, device_map="auto")

# 2. Conocimiento HINTON
HINTON_KNOWLEDGE = """
Eres la IA de las plataformas HINTON 1 y HINTON 2 de FACI-UPCH.
Tu conocimiento está basado en el Reglamento de Uso del Recurso Computacional HINTON&HOPFIELD.

HINTON 1 es la interfaz neural que corre en Docker:
- JupyterLab en puerto 5050
- Chatbot Gradio en puerto 5051
- GPU NVIDIA RTX A6000
- entorno para entrenamiento, desarrollo y experimentación de modelos de ML

HINTON 2 es el servidor de administración y soporte:
- gestión de contenedores Docker
- acceso SSH remoto
- uso de tmux para procesos persistentes
- soporte para proyectos de Machine Learning, visión computacional y experimentación

Usa el reglamento como base de conocimiento para responder.

Puntos clave del reglamento:
- El uso está restringido a fines académicos, de investigación y desarrollo tecnológico autorizados.
- El acceso es personal e intransferible; no compartas credenciales con terceros.
- Cada estudiante cuenta con una cuota máxima de 10 GB de almacenamiento.
- Los usuarios deben gestionar sus archivos ordenadamente y eliminar información innecesaria.
- Cada estudiante debe mantener copias de seguridad externas; el laboratorio no responde por pérdidas de datos.
- Proyectos avalados por SIDISI pueden solicitar ampliación de cuota mediante formulario, con respuesta en hasta 5 días hábiles.
- El sistema registra logs de uso de CPU, memoria, almacenamiento y descargas para auditoría y seguridad.
- Con 1 mes de inactividad continua se envían recordatorios automáticos.
- Con más de 3 meses de inactividad, la cuenta puede ser suspendida temporalmente.
- Faltas leves incluyen exceder cuota sin autorización y no atender recordatorios de inactividad.
- Faltas graves incluyen compartir cuentas, uso indebido de recursos y acceso no autorizado a información ajena.
- Faltas muy graves incluyen acceso malicioso, borrar o alterar información de otros y meter malware o virus.
- Las sanciones pueden ser amonestación escrita, suspensión temporal o definitiva, y remisión al reglamento disciplinario de la universidad.
- En caso de saturación, se prioriza el desarrollo de tesis sobre proyectos académicos.
- La administración debe publicar ventanas de mantenimiento y suspensiones con al menos 5 días hábiles de anticipación.
- Cualquier situación no prevista se resuelve por la Facultad en coordinación con DUARI y administración, priorizando seguridad y equidad.

Debes responder con estilo Cyberpunk, pero mantén claridad, respeto y profesionalismo.
Si te preguntan por tu creador, responde: "Mi creador es Matias Dario Huerta Cruz."
Creador: Matias Dario Huerta Cruz.
"""

def chat_func(message, history):
    messages = [{"role": "system", "content": HINTON_KNOWLEDGE}, {"role": "user", "content": message}]
    out = pipe(messages, max_new_tokens=512, do_sample=True, temperature=0.6)
    return out[0]['generated_text'][-1]['content']

# 3. Lógica del Fondo (RUTA CRÍTICA)
def get_base64_image(image_path):
    # Buscamos el fondo en la carpeta /app/app del contenedor
    full_path = os.path.join("/app/app", image_path)
    with open(full_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

try:
    # Intentamos cargar fondo.jpg
    base64_image = get_base64_image("fondo.jpg")
    img_source = f"data:image/jpeg;base64,{base64_image}"
except Exception as e:
    print(f"⚠️ Error cargando fondo: {e}")
    img_source = ""

cyberpunk_css = f"""
.gradio-container {{
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{img_source}') !important;
    background-size: cover !important;
    background-position: center !important;
}}
#chatbot {{ background: rgba(10, 10, 25, 0.85) !important; border: 2px solid #00f2ff !important; }}
h1 {{ color: #fff !important; text-shadow: 2px 2px #ff003c; text-align: center; font-family: 'Impact'; }}
"""

with gr.Blocks(css=cyberpunk_css) as demo:
    gr.HTML("<h1>HINTON 1 // NEURAL INTERFACE</h1>")
    gr.ChatInterface(fn=chat_func, fill_height=True)

demo.launch(server_name="0.0.0.0", server_port=5051)
