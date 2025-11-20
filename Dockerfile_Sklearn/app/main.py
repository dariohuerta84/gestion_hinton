import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

print('--- INICIANDO ENTRENAMIENTO ---')
model = LinearRegression()
model.fit(X, y)

prueba_x = [[10]]
prediccion = model.predict(prueba_x)

print(f'Entrenamiento finalizado.')
print(f'Si X es {prueba_x[0][0]}, el modelo predice Y = {prediccion[0]} (Esperamos 20)')
print('--- CEREBRO OPERATIVO ---')
