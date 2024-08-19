# Se importa la libreria de pandas.
import pandas as pd
import numpy as np

separador = '*'*50

# Se crea dicccionario
usuario = {
    'username': ['user1', 'user2', 'user3'],
    'email': ['user1@mail.com', 'user2@mail.com', 'user3@mail.com'],
    'age': [27, 10, 30],
    'status': [True, False, True]
}

a = pd.DataFrame(usuario)

print(separador)
print(a)
print(separador)

# Se le asignan los indices
a = pd.DataFrame(usuario, index=['a', 'b', 'c'])
print(a)
print(separador)

# mostrar solo lavolres de la columna
print(a['username'])
print(separador)

print(a['age'])
print(separador)

# mostrar el valor de un indice y una columna
print(a['username']['a'])
print(separador)

# otra forma de mostrar los valores de una columna
print(a.username)
print(separador)
print(a.email)
print(separador)

# se crea una serie
calificaciones = pd.Series(np.random.randint(5, 10, 3), index=['a', 'b', 'c'])

# se añade la columna
a['calificaciones'] = calificaciones

print(a)
print(separador)

# cambiar nombre de columna
a = a.rename(
    columns={'calificaciones': 'score'}
)

print(a)
print(separador)

# Eliminar una columna
del a['score']

print(a)
print(separador)
