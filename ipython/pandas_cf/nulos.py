# Pandas del curso de Codigo Facilito

import pandas as pd
import numpy as np

separador = '*'*30

# Se genera serie con valores nulos
a = pd.Series([1, 2, np.nan, np.nan, 5, 6, 7, np.nan, 8, 9])

print(separador)
print(a)
print(separador)
print(a.isnull())  # muestra que valores si son nulos con valores boleanos
print(separador)
print(a.notnull())  # muestra que valores no son nulos con valores boleanos
print(separador)
print(a[a.isnull()])  # muestra los indices que sean nulos
print(separador)
print(a[a.notnull()])  # muestra todos los indices que no son nulos
