# Pandas del curso de Codigo Facilito

import pandas as pd

# se genera diccionario
colores = {
    'rojo': 100,
    'verde': 200,
    'azul': 300,
    'negro': 400
}

a = pd.Series(colores)  # Pasamos como argumento un dicccionario.

print(a)
