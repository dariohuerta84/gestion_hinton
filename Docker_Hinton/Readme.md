para detener el contenedor usa
- sudo docker stop hinton_interactive_final
para reaundar el contenedor usa
- sudo docker start hinton_interactive_final
para eliminar el contenedor
- sudo docker rm -f hinton_interactive_final

🚀 Ejecutable Combinado (Puerto 5050)
Este comando mapea el puerto interno de Jupyter (8888) al puerto externo 5050 de tu servidor:

Bash

sudo docker build -t dockerfile_mc -f Dockerfile_MC/Dockerfile Dockerfile_MC && \
sudo docker rm -f docker_mc || true && \
sudo docker run -d --name docker_mc -p 5050:8888 \
-v /home/hinton1/Documents/ADMINISTRACION/repo/gestion_hinton/Dockerfile_MC:/app \
dockerfile_mc jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='' --NotebookApp.password=''