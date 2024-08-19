# Pandas del curso de Codigo Facilito

import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])

print(a)

print(a.dtype)  # tipo de dato de la serie

print(type(a))  # tipo de la serie

print(a.size)  # tmaño de la serie

print(a.shape)  # forma de serie

print(a.index)  # mostrar indices

print(a[4])  # obtener el valor de un indice

a[4] = 500  # LE asigno nuevo valor al indice

print(a)

b = pd.Series([1, 2, 3, 4, 5], index=[
              'a', 'b', 'c', 'd', 'e'])  # asignar el indice a los valores

print(b)

c = pd.Series([1, 2, 3, 4, 5],
              index=['a', 'b', 'c', 'd', 'e'],
              name='numeros'   # se le nombra la serie
              )

print(c)

d = pd.Series([1, 2, 3, 4, 5],
              index=['a', 'b', 'c', 'd', 'e'],
              name='numeros',
              dtype=str  # Sele asigna el tipo de datos de la serie
              )

print(d)
