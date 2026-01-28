import os
import sys
import torch

# 1. Configuración de rutas para encontrar la carpeta minGPT
directorio_actual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(directorio_actual, 'minGPT'))

from mingpt.model import GPT

# 2. Configuración del dispositivo (Usar GPU si está disponible)
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# 3. Reconstruir el vocabulario de caracteres (Debe ser idéntico al entrenamiento)
# Leemos tus apuntes para saber qué letras conoce el modelo
archivo_datos = os.path.join(directorio_actual, 'datos_entrenamiento.txt')
with open(archivo_datos, 'r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(list(set(text)))
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
vocab_size = len(chars)

# 4. Cargar la arquitectura y los pesos entrenados
print(f"Cargando modelo desde {device}...")
# Usamos gpt2 como base porque así lo guardamos en el fine-tuning
model = GPT.from_pretrained('gpt2')
ruta_pesos = os.path.join(directorio_actual, 'transformer_hinton_finetuned.pt')
model.load_state_dict(torch.load(ruta_pesos, map_location=device))
model.to(device)
model.eval()

# 5. Función para generar respuesta
def generar_respuesta(prompt, max_tokens=100):
    # Convertir el texto inicial a números (solo caracteres que el modelo conoce)
    x = torch.tensor([stoi[s] for s in prompt if s in stoi], dtype=torch.long)[None,...].to(device)
    
    # El modelo genera nuevos índices
    with torch.no_grad():
        y = model.generate(x, max_new_tokens=max_tokens, temperature=0.8, do_sample=True)
    
    # Convertir números de vuelta a texto
    resultado = ''.join([itos[int(i)] for i in y[0] if int(i) in itos])
    return resultado

# 6. Prueba de interacción
prompt_inicial = "En el futuro me gustaría"
print(f"\n--- Usuario: {prompt_inicial} ---")

respuesta = generar_respuesta(prompt_inicial)
print(f"\n--- Transformer: ---\n{respuesta}")