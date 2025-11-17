# gestion_hinton
"Un herediano mas comenzando una gestion de dockers"

Una prueba de que si funciona los cambios generados
"Matias Dario Huerta Cruz"
prueba desde mi lp

## Resumen 12 de noviembre 11:36

El contenedor arranca bien con Jupyter.

Monte mi carpeta local (Dockerfile_MC) para que los cambios se sincronicen.

Y pude ver mis archivos utilizados desde el navegador.

Comandos base

#### Ahora vamos a cancelar este proceso
sudo docker stop practical_proskuriakova

#### Si queremos utilizarlo de nuevo
sudo docker start practical_proskuriakova

### Comandos para arreglar branches
git checkout main
git fetch --all #esto actualiza las referencias remotas(sin mnzclar nada)
git push origin main --force #sobreescribe lo que hay en tu main local
