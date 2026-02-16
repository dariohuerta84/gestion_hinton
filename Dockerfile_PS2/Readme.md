# Usemos un ejemplo para demostar com funciona un docker
## Caso consola playstation vs pc
- VAMOS A DEFINIR COMO FUNCIONAN
- JUEGOS : TENEMOS PROYECTOS O JUEGOS QUE SON APP QUE FUNCIONAN CON UN SISTEMA CONFIGURADO
- PLAYSTATION : FUNCIONA COMO EL DOCKER (CONTENEDOR DE LOS PROYECTOS)
- PC : TENEMOS UNA PC DE ULTIMA GENERACION

## En este caso si queremos correr un videojuego de play station 2, por mas buena que sea la pc, tendra problemas de rendimiento y de fps, debido a que no esta optimizada, en cambio el contenedor (Playstation esta construido de manera asilada para poder emular y correr esos juegos)
- solucion ( crear un contenedor en una pc que contenga las librerias necesarias para poder emular un videojuego de play station 2)

1. ¿Por qué funcionaría bien en la HINTON I?

- Poder de Procesamiento: El CPU Core i9-14900K de 24 núcleos es ideal para la emulación, que depende mucho del rendimiento por núcleo.
- Aceleración Gráfica: La RTX A6000 permitiría escalar la resolución del juego original (480i) a 4K o más sin despeinarse, usando los núcleos CUDA del contenedor.

2. Retos Técnicos 
Para que esto funcione, no basta con instalar el emulador; el alumno tendría que configurar:

- X11 Forwarding / VNC: Como Docker es una "isla" sin pantalla propia, necesitaría una forma de transmitir la señal de video desde el contenedor hacia el monitor del usuario.
- Drivers de Video: Se deben instalar las librerías libgl1 y libxext6 dentro del Dockerfile (tal como lo hacemos en el entorno de Visión Computacional) para que el emulador pueda renderizar gráficos.
- Persistencia (Memory Card): Se usaría un volumen montado (-v) para que las partidas guardadas (BIOS y Memory Cards) vivan en el host de la HINTON y no se borren al cerrar el contenedor.


3. Aplicaicones Tecnicas

- CUDA (Compute Unified Device Architecture) es una plataforma de computación paralela y modelo de programación creado por NVIDIA que permite utilizar la unidad de procesamiento gráfico (GPU) para tareas de propósito general, no solo gráficos. 
- CUDA transforma la GPU en un motor de computación de alto rendimiento, logrando velocidades mucho mayores que las CPUs convencionales en tareas repetitivas y paralelas. 
- La dependencia X11 (X Window System) es un sistema de ventanas base para interfaces gráficas (GUI) en sistemas Unix/Linux, a menudo requerido por aplicaciones como libx11-dev para compilar o ejecutar software.
- OpenGL (Open Graphics Library) es una API estándar, multiplataforma y de código abierto que permite a los desarrolladores renderizar gráficos 2D y 3D


4. El Comando de Ejecución (La Regla de Oro)
- Para que el alumno vea el juego, debe conectar el contenedor con el sistema gráfico (X11) de la PC. El comando para la HINTON I sería:

sudo docker run -it \
  --name docker_ps2_edu \
  --gpus all \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /home/hinton1/Documents/PS2/games:/app/games \
  -v /home/hinton1/Documents/PS2/memcards:/app/memcards \
  --device /dev/snd \
  opencv-jupyter:v1

## ¿Qué está pasando aquí? :

- --gpus all: Le da al emulador el poder de los 49GB de VRAM de la RTX A6000 para escalar la resolución.

- -e DISPLAY: Es el "cable virtual" que conecta la consola (Docker) al televisor (Monitor de la HINTON).

- -v (Volúmenes): Garantiza la Persistencia Absoluta. Si el alumno borra el contenedor, sus partidas guardadas y sus juegos siguen intactos en el host.

- --device /dev/snd: Mapea el hardware de sonido para que el juego tenga audio.