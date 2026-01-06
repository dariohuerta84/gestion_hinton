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

# Comenzando con el tema administrativo en la deteccion de usuarios que utilicen la hinton 1 y 2

### Uso de comandos linux y tmux:

## Comandos linux:
- sudo docker ps -a	     ---      // Muestra todos los contenedores (activos, detenidos y salidos).	
Se usa para encontrar el ID o nombre de contenedores detenidos que necesitan ser eliminados o reiniciados. 

- sudo docker stop ID	 ---          // Detiene un contenedor en ejecución (por ID o nombre).	
Se usa para pausar el entorno de desarrollo interactivo Dockerfile_MC. 

- sudo docker start ID	 ---      // Reinicia un contenedor que ha sido detenido.	
Se usa para reanudar el entorno persistente Dockerfile_MC. 

- sudo docker rm ID	     ---      // Elimina un contenedor que se encuentra detenido (por ID o nombre).	
Parte del proceso de limpieza para liberar recursos. 

- sudo docker rm -f Nombre	---   // Fuerza la eliminación de un contenedor, deteniéndolo si es necesario.	
Útil para eliminar contenedores que no responden.

- ssh hinton2@Dirección_IP --- // Este comando sirve para cambiar el usuario a el otro hinton en este caso

## Comandos tmux:
- tmux ls	              ---                // Muestra una lista de todas las sesiones de Tmux activas.	
Te permite verificar los nombres de las sesiones disponibles (ej., tmux_victoria).

- tmux new -s nombre_sesion	  ---        // Crea una nueva sesión de Tmux con el nombre especificado.	
Inicia un nuevo espacio de trabajo aislado y persistente.

- tmux attach -t nombre_sesion	 ---     // Se adjunta (regresa) a una sesión de Tmux que ya existe.	
Te devuelve al estado exacto de tu trabajo, incluso después de desconexiones.

- Ctrl-b d	            ---              // Atajo de teclado para desadjuntar (separar) la sesión actual.	
Es la forma segura de salir sin detener los procesos que corren dentro de ella.

- tmux kill-session -t tmux_victoria   --- // Con este comando se elimia la sesion de tmux, asegurarse de no estar dentro del tmux, primero salir de la secion

# Detener el contenedor de Visión
sudo docker stop docker_opencv

# Detener el contenedor de Pruebas Ligeras
sudo docker stop docker_limited

| Dockers | Contenido | Función | Puerto | ¿Tiene Jupyter? |
| :--- | :--- | :--- | :--- | :--- |
| **DockerFile** | Python basic | Demostrar el funcionamiento básico de construcción (build) y ejecución (run) de un contenedor que imprime un mensaje de saludo. | No necesita | No |
| **DockerFile_MC** | NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn y Jupyter Deep Learning: TensorFlow y PyTorch. | Proporcionar un IDE web interactivo con sincronización bidireccional de archivos mediante volúmenes. | 8888 | Sí |
| **DockerFile_MC2** | Pytorch y Numpy. Sistema: build essential. | Ejecutar un pipeline completo de entrenamiento en un contenedor efímero que se auto-elimina al terminar. | No utiliza | No |
| **docker_opencv** | opencv-python-headless, numpy, matplotlib, imutils. | Proporcionar un entorno especializado para el procesamiento de imágenes y visión computacional, optimizado para ligereza. | 8889 | Sí |
| **DockerFile_SKlearn** | Scikit-learn, Pandas y NumPy. | Validar la instalación de la pila de ML y realizar pruebas de concepto (PoC) como regresiones lineales simples. | 5000 | No |
| **docker_limited** | Jupyter, NumPy y Pandas. | Entorno interactivo ligero para pruebas rápidas de datos, transformado desde un servidor Nginx. | 8890 | Sí |