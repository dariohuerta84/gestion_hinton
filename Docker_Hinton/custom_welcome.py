import torch
import os
import psutil

def show_welcome():
    japonese_msg = "「大丈夫、勝つから」" # Nah, I'd win
    
    print("\n" + "═"*60)
    print("      ESTACIÓN DE TRABAJO HINTON I - FACI UPCH")
    print("═"*60)
    print(f"\n   {japonese_msg}")
    print("      (Nah, yo ganaré)\n")
    
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        # Usamos propiedades del dispositivo para la VRAM
        props = torch.cuda.get_device_properties(0)
        vram_total = props.total_memory / 1024**3
        print(f"🚀 GPU: {gpu_name} detectada.")
        print(f"📊 VRAM: {vram_total:.2f} GB totales para entrenamiento.")
    else:
        print("❌ ALERTA: La GPU no está siendo reconocida por el contenedor.")

    cpu_cores = os.cpu_count()
    ram_gb = psutil.virtual_memory().total / (1024**3)
    print(f"💻 CPU: i9-14900K con {cpu_cores} núcleos/hilos.")
    print(f"🧠 RAM: {ram_gb:.2f} GB DDR5 activa.")
    print("-" * 60)
    print("Iniciando JupyterLab en el puerto 5050...")
    print("═"*60 + "\n")

if __name__ == "__main__":
    show_welcome()