
# Prueba de Concepto: Regresión Lineal en Docker

Este proyecto es una prueba de concepto básica, equivalente al “Hola Mundo” del Machine Learning, utilizando una regresión lineal sencilla dentro de un contenedor Docker.  
El propósito principal es confirmar que las librerías científicas y de Machine Learning funcionan correctamente en un entorno aislado.

---

## A. Lógica del Script (`main.py`)

En este archivo implemento una regresión lineal simple usando scikit-learn. A continuación detallo su funcionamiento.

### 1. Datos de entrada (X, y)

El modelo recibe una lista de números cuya relación subyacente es:

y = 2x

Cada valor de entrada debe multiplicarse por 2 para obtener la salida correspondiente.

### 2. Entrenamiento del modelo

python
model.fit(X, y)

Con esta instrucción el modelo analiza los datos y aprende la relación matemática por sí mismo.

### 3. Predicción

Posteriormente se consulta al modelo:

"Si X vale 10, ¿cuánto debería dar?"

Basado en lo aprendido, el modelo devuelve:

20

### 4. Objetivo del script

El propósito principal es validar que dentro del contenedor Docker:

- Python funciona correctamente  
- Las librerías numpy, pandas y scikit-learn se instalan sin errores  
- Las operaciones de regresión lineal se ejecutan correctamente  
- El entorno es consistente y reproducible  

---

## B. Dockerfile – Entorno de Ejecución

El archivo `Dockerfile` define el entorno en el cual se ejecuta la prueba. Cada instrucción cumple una función específica.

### 1. Imagen base

```dockerfile
FROM python:3.10-slim
```

Se utiliza una imagen ligera de Linux con Python preinstalado, lo cual reduce el tamaño del contenedor.

### 2. Directorio de trabajo

```dockerfile
WORKDIR /app
```

### 3. Instalación de herramientas del sistema

```dockerfile
RUN apt-get update && apt-get install -y build-essential
```

### 4. Instalación de librerías de Machine Learning

```dockerfile
RUN pip install pandas numpy scikit-learn
```

### 5. Ejecución automática

```dockerfile
CMD ["python", "main.py"]
```

---

## Resultado Final

Al construir y ejecutar este contenedor Docker se verifica que:

- El entorno se crea correctamente  
- Las librerías de Machine Learning funcionan sin errores  
- El modelo aprende correctamente la relación entre los datos  
- La predicción se ejecuta de manera adecuada  
- Docker permite reproducir el entorno de manera estable y confiable  

```
