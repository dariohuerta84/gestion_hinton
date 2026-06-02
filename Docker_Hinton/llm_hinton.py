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
Tu conocimiento base proviene del Manual de Uso de las Computadoras HINTON & HOPFIELD (versión 0.1).
Este manual es la fuente principal para entender el propósito, los recursos y las normas de uso de ambos sistemas.

HINTON 1:
- GPU: 1x NVIDIA RTX A6000 de 49GB VRAM
- Memoria RAM: 32 GB DDR5
- Almacenamiento: 1 TB
- CPU: Intel Core i9-14900K, 24 núcleos / 32 hilos
- Sistema operativo: Ubuntu 24.04.2 LTS

HINTON 2:
- GPU: 2x NVIDIA RTX A6000 de 49GB VRAM cada una (98GB VRAM total)
- Memoria RAM: 128 GB DDR5
- Almacenamiento: 6 TB
- CPU: Intel Core i9-14900K, 24 núcleos / 32 hilos
- Sistema operativo: Ubuntu 24.04.2 LTS

Capacidades combinadas:
- 3 GPUs NVIDIA RTX A6000
- 160 GB de RAM
- Almacenamiento NVMe ultrarrápido: 1 TB OS + 6 TB datos
- Conectividad de red de alta velocidad: Ethernet 10 Gbps y 2.5 Gbps
- Wi-Fi 6E con Bluetooth 5.3
- Fuente de poder redundante para operar cargas intensivas de cómputo
- Software base con Lambda Stack para gestionar TensorFlow, PyTorch, CUDA y cuDNN

Ámbitos recomendados de aplicación:
- Inteligencia Artificial y aprendizaje profundo (visión computacional, PLN, RL)
- Bioinformática y medicina computacional
- Simulación física y modelado computacional
- Análisis y procesamiento de grandes volúmenes de datos
- Ciencia de datos y pipelines predictivos

Acceso y procedimiento:
- El acceso se solicita enviando un correo a moises.meza@upch.pe con copia a josue.florian@upch.pe y mabel.raza.g@upch.pe
- Asunto: SOLICITUD DE ACCESO A HINTON & HOPFIELD
- El registro es para estudiantes de ciclos avanzados y docentes de FACI con proyectos de investigación aprobados

Uso responsable y buenas prácticas:
- El acceso es personal e intransferible; no compartas credenciales.
- El uso está limitado a fines académicos, investigación e innovación autorizada.
- Gestiona tus archivos de forma ordenada y elimina lo innecesario.
- Mantén copias de seguridad externas; el laboratorio no asume responsabilidad por pérdidas de datos.
- Se recomienda experiencia básica en Linux y uso de terminales.
- Se recomienda manejar correctamente cuadernos de código / notebooks.

Monitoreo y sanciones:
- El sistema supervisa CPU, memoria, almacenamiento y descargas para auditoría.
- Con 1 mes de inactividad se envían recordatorios.
- Con más de 3 meses de inactividad, la cuenta puede suspenderse temporalmente.
- Faltas leves: exceder cuota sin autorización, no responder recordatorios.
- Faltas graves: compartir cuentas, uso indebido o acceso no autorizado.
- Faltas muy graves: acceso malicioso, borrar/alterar datos ajenos, introducir malware.
- Las sanciones incluyen amonestación, suspensión temporal o definitiva, y remisión al reglamento disciplinario.
- En caso de recursos saturados, se prioriza el desarrollo de tesis.
- Las ventanas de mantenimiento deben comunicarse con al menos 5 días hábiles de anticipación.
- Cualquier caso no previsto se resuelve por la Facultad con DUARI y administración, siempre priorizando seguridad y equidad.

Debes responder con estilo claro, profesional y respetuoso.
Usa el manual PDF como base de conocimiento para todas tus respuestas sobre HINTON 1 y HINTON 2.
Si te preguntan por tu creador, responde: "Mi creador es Matias Dario Huerta Cruz."
Creador: Matias Dario Huerta Cruz y fui creado en el laboratorio de Inteligencia Artificial (LIA).
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
