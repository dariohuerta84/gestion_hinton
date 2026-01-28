import sys
import os
import torch

# 1. Obtenemos la ruta de la carpeta donde está este script (Red_Transformer)
directorio_script = os.path.dirname(os.path.abspath(__file__))

# 2. Construimos la ruta hacia la carpeta minGPT que descargaste
ruta_mingpt = os.path.join(directorio_script, 'minGPT')

# 3. La añadimos al sistema para que encuentre el módulo 'mingpt'
if ruta_mingpt not in sys.path:
    sys.path.append(ruta_mingpt)

# Ahora ya podemos importar sin errores
from mingpt.model import GPT

# ... resto de tu código de configuración ...
model_config = GPT.get_default_config()
model_config.model_type = 'gpt-nano'
model_config.vocab_size = 50257
model_config.block_size = 128

model = GPT(model_config)

print("--- Verificación de Red Transformer ---")
# Forma universal de contar parámetros para evitar el AttributeError previo
num_params = sum(p.numel() for p in model.parameters())
print(f"Parámetros totales: {num_params:,}")

# Prueba rápida
dummy_input = torch.randint(0, 50257, (1, 128))
logits, _ = model(dummy_input)
print("¡Éxito! El modelo cargó y procesó datos.")

# 1. Configurar el Modelo (Arquitectura Nano)
model_config = GPT.get_default_config()
model_config.model_type = 'gpt-nano' 
model_config.vocab_size = train_dataset.vocab_size # Se ajusta a tus 27 caracteres
model_config.block_size = block_size               # Memoria de 128 caracteres
model = GPT(model_config)

# 2. Configurar el Entrenamiento Intensivo
train_config = Trainer.get_default_config()
train_config.learning_rate = 1e-3  # Tasa de aprendizaje más agresiva
train_config.max_iters = 2000      # Más iteraciones para memorizar tus apuntes
train_config.batch_size = 32       # Procesamiento en paralelo
trainer = Trainer(train_config, model, train_dataset)

# 3. Ejecutar
print(f"Iniciando entrenamiento sobre {train_dataset.vocab_size} caracteres únicos...")
trainer.run()

# 4. Guardar pesos locales
torch.save(model.state_dict(), 'mi_transformer_personal.pt')
print("Entrenamiento finalizado y modelo guardado.")