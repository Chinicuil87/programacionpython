import pandas as pd
import numpy as np

separador = ('*'*100)

# importamos
data = pd.read_csv('pandas_cf/users.csv')

print(separador)
print(data)
print(separador)

# se asigna una columna como indice
data = pd.read_csv('pandas_cf/users.csv', index_col='id')
print(data)
print(separador)

# muestra los primeras 5 filas de nuetros datos
print(data.head())
print(separador)

# muetra el numero de filas deseado
print(data.head(20))
print(separador)

# muetsra las ultimas 5 filas
print(data.tail())
print(separador)

# muestra las ultimas filias deseadas
print(data.tail(10))
print(separador)

# Elinina las filas que tengan valor nulo
# print(data.head(10))
# data = data.dropna()
# print(separador)
# print(separador)
# print(data.head(10))
# print(separador)


# print(data.head(10))
# print(separador)
# print(separador)
# # cambia el valor de los nulos
# data = data.fillna('Nuevo valor')
# print(data.head(10))
# print(separador)


print(data.head(10))
data = data.fillna({'nombre': 'Sin nombre', 'email': 'Sin email'})
print(separador)
print(separador)
print(data.head(10))
print(separador)
