import torch
from transformers import pipeline

# Verificación de la Energía Maldita (GPU)
device = "cuda" if torch.cuda.is_available() else "cpu" [cite: 1417]
print(f"🔮 Canalizando poder a través de: {torch.cuda.get_device_name(0)}") [cite: 1389]

# Cargando un modelo de lenguaje (Ejemplo: TinyLlama)
# Con 48GB de VRAM, ¡podrías cargar modelos mucho más grandes!
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", device=0)

prompt = "Vez que si funciona el Docker? Cosas como estas puedes hacer en la HINTON 1. ¿Qué opinas?"

outputs = pipe(prompt, max_new_tokens=100, do_sample=True, temperature=0.7)
print(f"\n💬 RESPUESTA DEL LLM:\n{outputs[0]['generated_text']}")