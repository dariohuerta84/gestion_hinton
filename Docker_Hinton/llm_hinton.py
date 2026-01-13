import gradio as gr
import torch
from transformers import pipeline
import base64
import os

# 1. IA Core
model_id = "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit"
pipe = pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")

# 2. Conocimiento HINTON
HINTON_KNOWLEDGE = "Eres la IA de la HINTON 1. Responde con estilo Cyberpunk y usa el reglamento de la UPCH."

def chat_func(message, history):
    messages = [{"role": "system", "content": HINTON_KNOWLEDGE}, {"role": "user", "content": message}]
    out = pipe(messages, max_new_tokens=512, do_sample=True, temperature=0.6)
    return out[0]['generated_text'][-1]['content']

# 3. Lógica del Fondo (RUTA CRÍTICA)
def get_base64_image(image_path):
    # Buscamos el fondo en la carpeta /app del contenedor
    full_path = os.path.join("/app", image_path)
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
