- ### Aca vamos a comenzar con la creacion de otro dockerfile con machine learning

- ##Comenzamos con la creacion de nuestro dockerfile y una carpeta app la cual tendra el main.py
- mkdir -p Dockerfile_MC2/app
- touch Dockerfile_MC2/Dockerfile
- touch Dockerfile_MC2/requirements.txt
- touch Dockerfile_MC2/app/main.py

### Vamos a trabajar con pytorch
- Pytorch es un framework de deep learning creado por Facebook (Meta).

Es actualmente el más usado por investigadores y desarrolladores por ser:

- intuitivo: se programa como Python puro; no obliga a usar grafos estáticos.
- rápido para prototipar: ideal para pruebas, modelos nuevos, investigación.
- muy flexible: puedes modificar la arquitectura del modelo fácilmente.
- con gran soporte en la industria (Meta, Tesla, OpenAI, Microsoft Research).

### Para qué se usa comúnmente

- Redes neuronales profundas (DNNs)
- Redes convolucionales (CNN) → visión computacional
- Redes recurrentes / transformadores → NLP
- Modelos de time series avanzados
- Reinforcement 

## En este caso trabajare con redes neuronales pequeñas, para paractiar.

### En el text agregare:
- numpy
torch==2.2.0

### Y luego en el main ira un script el cual
Genera datos,
Crea la red,
Entrena,
Calcula gradientes,
Optimiza,
Imprime resultados.

### Asegurarse que estas en la carpeta:
- cd Dockerfile_MC2

### Vamos a construir la imagen con este comando:
- cd DockerNN
sudo docker build -t nn-container:v1 .

### vamos a ejecutarlo dentro del docker
- sudo docker run --rm nn-container:v1
