# gestion_hinton
"Un herediano mas comenzando una gestion de dockers"

Una prueba de que si funciona los cambios generados
"Matias Dario Huerta Cruz"
prueba desde mi lp

---
## Resumen 12 de noviembre 11:36

El contenedor arranca bien con Jupyter.

Monte mi carpeta local (Dockerfile_MC) para que los cambios se sincronicen.

Y pude ver mis archivos utilizados desde el navegador.

Comandos base
---


#### Ahora vamos a cancelar este proceso
- sudo docker stop practical_proskuriakova     
   
#### Si queremos utilizarlo de nuevo
- sudo docker start practical_proskuriakova

### Comandos para arreglar branches
- git checkout main
- git fetch --all #esto actualiza las referencias remotas(sin mnzclar nada)
- git push origin main --force #sobreescribe lo que hay en tu main local

### Comando para visualizar tu imagen de docker:
- sudo docker images
### Para saber donde esta corriendo cuando lo ejecutas:
- sudo docker ps


---
## Resumen 17 de noviembre 11:46

- Mi Resumen del Trabajo Realizado
He logrado establecer mi entorno de Machine Learning completamente en Docker, utilizando PyTorch, y esta fue la trayectoria:
- Elegí un Docker orientado a Machine Learning: 
- Mi objetivo era claro: necesitaba un contenedor diseñado para entrenar redes neuronales, no para servir páginas web. Por eso, decidí que no utilizaría puertos.
- La Decisión fue PyTorch (solo CPU): Me incliné por PyTorch (versión torch==2.2.0) en lugar de TensorFlow. La razón es que no necesito GPU, estoy enfocado en el aprendizaje y en hacer pruebas rápidas con modelos pequeños, y PyTorch CPU-only es mucho más liviano para este propósito.Creé la Estructura del Proyecto:
- Organicé todo de manera limpia dentro de la carpeta Dockerfile_MC2

Esta estructura es mi entorno completo de ML dentro del contenedor.
- Configuré las Dependencias Esenciales: En requirements.txt solo incluí lo necesario para mantener el contenedor ligero:numpytorch==2.2.0
- Desarrollé un Script de Entrenamiento Funcional: En app/main.py, tengo un código que valida mi entorno. 
- Este script:Genera datos sintéticos simples ($y = 3x + 2$).Construye una Red Neuronal Multicapa (MLP) muy básica.Entrena la red durante varias épocas.Muestra la pérdida (loss) en la terminal.Imprime una predicción final.
- Ajusté el Dockerfile para ser Operativo y Liviano: Mi Dockerfile actual utiliza python:3.10-slim, instala las dependencias de sistema y Python, copia mi proyecto y, crucialmente, tiene un comando de entrada que ejecuta automáticamente python app/main.py.
- Confirmé que NO usa Puertos: Esto es una característica clave. Como el contenedor solo ejecuta una tarea de entrenamiento y finaliza, no es un servidor. Se ejecuta y termina sin publicar endpoints ni requerir configuración de puertos.Comprendí el Almacenamiento: Mi código fuente y Dockerfile están en gestion_hinton/Dockerfile_MC2. 
- La imagen Docker binaria se almacena internamente en /var/lib/docker y puedo verificarla con sudo docker images.
- El Resultado Final es que ya tengo un Docker de Machine Learning completamente funcional, reproducible, liviano y listo para entrenar mi primera red neuronal en un entorno encapsulado.
---



# Uso de Scikit-learn y que es?
- Es una biblioteca importante de python, especializada en el uso de machine learning.
- Se usa para algoritmos de clasificación, regresión y agrupación.

# Continuaciones y actualizaciones:
- Creacion de dockerhub
- Analisis del nuevo Neested learnig
- cambiar de github.com/repositorio a deepwiki.com/repositorio para resumir repos
- Conocimientos aceca de Radware 

