# Aca comenzaremos con la instalacion, para lo que necesitaremops instalar panda y numpys scikit-learn, incluso tensorflow o pytorch
Creamos un archico llamado dockerfile y pegamos estos codigos

## Imagen base ligera de Python
FROM python:3.10-slim

## Establecer el directorio de trabajo
WORKDIR /app

## Copiar los archivos del proyecto
COPY . /app

## Instalar dependencias del sistema (por si algunas libs lo necesitan)
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

## Instalar librerías de Machine Learning
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    scikit-learn \
    matplotlib \
    seaborn \
    jupyter

## Si quieres usar TensorFlow o PyTorch (opcional):
RUN pip install tensorflow
RUN pip install torch torchvision torchaudio

## Exponer el puerto de Jupyter Notebook
EXPOSE 8888

## Comando por defecto (inicia Jupyter Notebook)
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# luego abrimos el terminal desde ~/Documents/ADMINISTRACION/repo/gestion_hinton$ y pegamos este comando
sudo docker build -t ml-env:v1 -f Dockerfile_MC/dockerfile .

Esto hará que Docker lea tu archivo línea por línea y cree una imagen.
Verás que va descargando Python, instalando librerías, etc.

esperamos a que termine la instalacion y luego colocamos este comando
sudo docker run -p 8888:8888 ml-env:v1

Eso lanza tu contenedor y abre Jupyter Notebook adentro.
La terminal te mostrará un link con un token, como:
 http://127.0.0.1:8888/tree?token=facaf891c97de653108b5e487d8533e2db4100285040cf2f

 Si llegas a visualizar una pagina de jupiter con todos tus archivos 
 Eso significa que tu contenedor de machine learning está corriendo perfecto, y que tu entorno de trabajo dentro de Jupyter ya se conectó a los archivos locales (vía el COPY . /app del Dockerfile).

Ahora estás trabajando dentro del contenedor, pero con tus propios documentos. Todo lo que crees o modifiques ahí quedará dentro de la imagen (a menos que montes tu carpeta local como volumen, si quieres que se guarden afuera).

Para que ambos lados vean lo mismo (tu host y el contenedor), necesitas montar tu carpeta local como un volumen cuando ejecutas el contenedor.
sudo docker run -p 8888:8888 -v "$(pwd)/Dockerfile_MC:/app" ml-env:v1

tuve un error con la actualizacion de cambios y tuve que detener y eliminar ese docker para ejecutarlo de nuevo

# Detener el comando
sudo docker stop 1988cf2d14ee

# Eliminacion
sudo docker rm 1988cf2d14ee

# Reejecucion
sudo docker run -p 8888:8888 -v "$(pwd)/Dockerfile_MC:/app" ml-env:v1

cambio abrusco esperar eliminacion del checkpoint
problema solucionado desde github, ya que me pedia permisos extras desde aca
bueno sigamos desde aqui
ah--- paso de todo xd

##espera esto lo escribi desde jupiter
## este texto fue escrito desde jupiter y se pudo guardar en mi visual

# Ahora vamos a cancelar este proceso
sudo docker stop practical_proskuriakova

# Si queremos utilizarlo de nuevo
sudo docker start practical_proskuriakova


# Para dejar el docker completamente limpio
1. Solo eliminar el contenedor actual

sudo docker ps

En tu caso:

e563c7e99aae   ml-env:v1   ...

Entonces lo detenés y eliminás:

sudo docker stop e563c7e99aae
sudo docker rm e563c7e99aae

 2. También eliminar la imagen (para reinstalar desde cero)

sudo docker rmi ml-env:v1

(Esto borra la imagen que construiste a partir del Dockerfile)

 3. Limpieza completa (contenedores, imágenes, volúmenes, caché)

Si querés dejar Docker totalmente limpio:

sudo docker system prune -a --volumes

4. comando para ver la imagen 
sudo docker images

Puntos donde hubo más complicaciones

Autenticación de GitHub (token) → error común tras eliminar contraseña tradicional.

Sincronización de ramas (main vs master y commits divergentes).

Errores 403 de Jupyter por permisos al montar la carpeta local.