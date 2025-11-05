Comencemos con los dockers:
Los dockers son plataformas de codigos abiertos los cuales ayudaran con la creación, despliegue y la ejecución de aplicaciones a base de contenedores.

Si una máquina virtual (VM) es un apartamento completo (con su propio sistema operativo), un contenedor Docker es un camarote de un crucero: usa los recursos comunes del barco (el sistema operativo del host), pero es totalmente aislado y contiene todo lo necesario para esa estancia específica.

Comencemos con las caracteristicas principales de los dockers o para que serian de gran utilidad:
- Aislamiento : No interfiere con procesos externos, como el sistema operativo o otros contenedores.
- Portabilidad : Los contenedores son ligeros y pueden moverse fácilmente entre diferentes hosts y sistemas operativos (Windows, Linux, Mac).
- Inmutabilidad : Las imágenes de Docker se construyen a partir de un Dockerfile y son inmutables (no cambian). Las modificaciones se realizan creando una nueva imagen.


Conceptos a practicar: 
- DockerFile : Un archivo de texto con instrucciones para generar una imagen en Docker
- La Imagen : Una plantilla de una lectura donde se puedan ver todas las capas para ejecutar una apliación
- Contenedor : Es una instancia en ejecución de una Imagen de Docker. Es donde el software cobra vida. Puedes iniciar, detener, mover y eliminar contenedores.
- Proxy Inverso : Es un servidor que se sitúa entre los clientes e internet, actuando como un intermediario que recibe todas las solicitudes de los clientes antes de redirigirlas a los servidores web correspondientes. Esto proporciona beneficios como la mejora de la seguridad, el aumento del rendimiento, la escalabilidad y la optimización del tráfico.

Ejemplo de comando en Ngix donde se ejecutara un contenedor en el puerto 8000
# docker run -d -p 8000:80 nginx

docker run : Le dice a Docker que tome una imagen y cree un Contenedor a partir de ella para ejecutarla.
-d : Modo de ejecución: Ejecuta el contenedor en segundo plano (detached mode). Esto significa que el contenedor se inicia, pero libera tu terminal para que puedas seguir usándola.
-p 8000:80 : Mapea un puerto de tu máquina anfitriona (Ubuntu) a un puerto dentro del contenedor.
nginx: Le indica a Docker que descargue y use la imagen oficial del servidor web Nginx (por defecto, usa la etiqueta latest).

Pero, para que sirve este comando exactamente? 
- Tiene un propósito muy específico: ejecutar un servidor web Nginx de forma instantánea y aislada.

El comando inicia un Contenedor que ejecuta el servidor web Nginx. Este servidor web es una herramienta muy popular para servir contenido estático (HTML, CSS, imágenes) y actuar como un proxy inverso.

1. Servidor Listo en Segundos
Lo que hace es encapsular y ejecutar toda la configuración necesaria para que Nginx funcione. 

Sin Docker, instalar y configurar Nginx en tu sistema operativo Ubuntu requeriría varios comandos, descargas de dependencias y configuración manual.
Con Docker: El comando hace todo eso por ti en un solo paso, utilizando la imagen preconfigurada de Nginx.

Pasos para poder Instalar con docker: