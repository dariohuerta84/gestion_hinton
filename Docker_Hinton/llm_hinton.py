import gradio as gr
import torch
from transformers import pipeline
import base64
import os

# 1. IA Core
model_id = "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit"
hf_token = os.getenv("HF_TOKEN")
if hf_token:
    print("✅ Usando HF_TOKEN para autenticación en Hugging Face")
else:
    print("⚠️ No se detectó HF_TOKEN; la descarga será anónima y con límites de tasa más bajos")
pipe = pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"dtype": torch.bfloat16},
    device_map="auto",
    use_auth_token=hf_token if hf_token else None,
)

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
Creador: Matias Dario Huerta Cruz y fui creado en el laboratorio de Inteligencia Artificial (LIA) en la UPCH Universiad Peruana Cayetano Heredia
"""

def build_prompt(message):
    return (
        f"{HINTON_KNOWLEDGE}\n\n"
        f"Usuario: {message}\n"
        "IA:"
    )


def chat_func(message, history):
    prompt = build_prompt(message)
    out = pipe(
        prompt,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
        return_full_text=False,
    )
    # El pipeline de text-generation devuelve una lista con generated_text
    response = out[0]["generated_text"] if isinstance(out, list) else out["generated_text"]
    return response.strip()

# 3. Interfaz con logo centrado

def get_logo_base64(image_name):
    for base_path in ["/app", "/app/app", os.getcwd()]:
        logo_path = os.path.join(base_path, image_name)
        if os.path.exists(logo_path):
            with open(logo_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")
    return None

logo_base64 = get_logo_base64("logoupch.jpg")
if not logo_base64:
    print("⚠️ logoupch.jpg no se encontró en /app, /app/app o directorio actual")
logo_url = f"data:image/jpeg;base64,{logo_base64}" if logo_base64 else ""

cyberpunk_css = f"""
body, html, .gradio-app, .gradio-container {{
    background-color: #ffffff !important;
    background-image: url('{logo_url}') !important;
    background-repeat: no-repeat !important;
    background-position: center center !important;
    background-attachment: fixed !important;
    background-size: auto !important;
    min-height: 100vh !important;
}}
#chatbot {{
    background: rgba(255, 255, 255, 0.9) !important;
    border: 2px solid #000000 !important;
}}
h1 {{
    color: #000000 !important;
    text-shadow: none !important;
    text-align: center;
    font-family: 'Impact';
}}
"""

with gr.Blocks(css=cyberpunk_css) as demo:
    gr.HTML("<h1>HINTON 1 // NEURAL INTERFACE</h1>")
    gr.ChatInterface(fn=chat_func, fill_height=True)

demo.launch(server_name="0.0.0.0", server_port=5051)
