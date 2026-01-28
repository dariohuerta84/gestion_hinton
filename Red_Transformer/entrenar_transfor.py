import os
import sys
import torch
from torch.utils.data import Dataset

# Rutas para minGPT
sys.path.append(os.path.join(os.path.dirname(__file__), 'minGPT'))
from mingpt.model import GPT
from mingpt.trainer import Trainer

# 1. Dataset (Usaremos el mismo CharDataset que ya tienes)
class CharDataset(Dataset):
    def __init__(self, data, block_size):
        chars = sorted(list(set(data)))
        self.stoi = { ch:i for i,ch in enumerate(chars) }
        self.itos = { i:ch for i,ch in enumerate(chars) }
        self.block_size = block_size
        self.vocab_size = len(chars)
        self.data = data

    def __len__(self):
        return len(self.data) - self.block_size

    def __getitem__(self, idx):
        chunk = self.data[idx:idx + self.block_size + 1]
        dix = [self.stoi[s] for s in chunk]
        x = torch.tensor(dix[:-1], dtype=torch.long)
        y = torch.tensor(dix[1:], dtype=torch.long)
        return x, y

# Leer tus apuntes técnicos
text = open('datos_entrenamiento.txt', 'r').read()
block_size = 128 
train_dataset = CharDataset(text, block_size)

# 2. CARGAR MODELO PRE-ENTRENADO (Aquí ocurre la magia)
print("Cargando pesos pre-entrenados de GPT-2...")
model = GPT.from_pretrained('gpt2') 
# Nota: GPT2 original usa un vocabulario de 50257 tokens. 
# Para un fine-tuning estricto sobre tus caracteres, el 'gpt-nano' es mejor,
# pero usar 'from_pretrained' requiere que el modelo sea compatible con GPT2.

# 3. Configurar entrenamiento ligero
train_config = Trainer.get_default_config()
train_config.learning_rate = 1e-5 # Tasa mucho más baja para no "borrar" lo que ya sabe
train_config.max_iters = 200      # Pocas iteraciones bastan para ajustar
batch_size = 8
trainer = Trainer(train_config, model, train_dataset)

print("Iniciando Fine-tuning...")
trainer.run()

# 4. Guardar el modelo ajustado
torch.save(model.state_dict(), 'transformer_hinton_finetuned.pt')
print("Modelo guardado como 'transformer_hinton_finetuned.pt'")