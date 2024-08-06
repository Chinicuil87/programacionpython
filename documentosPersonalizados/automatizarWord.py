# Importamos modulos
import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

# Leemos la plantilla de Word
doc = DocxTemplate('plantilla.docx')

# Generamos las variables.
nombre = ' Cesar Lopez'
telefono = '7227580505'
correo = 'clopezorihuela@hotmail.com'
fecha = datetime.today().strftime("%d/%m/%Y")

print(fecha)

# Asignamos las variables aun disccionario.
constantes = {'nombre': nombre,
              'telefono': telefono,
              'correo': correo,
              'fecha': fecha}

print(constantes)

doc.render(constantes)
doc.save(f"prueba.docx")


df = pd.read_excel('datos.xlsx')

print(df)

for indice, fila in df.iterrows():
    contenido = {
        'user': fila["Nombre_usuario"],
        'edad': fila["Edad"],
        'ingreso': fila["Fecha Ingreso"]
    }
    contenido.update(constantes)
    print(contenido)

    doc.render(contenido)
    doc.save(f"Prueba_{fila["Nombre_usuario"]}.docx")
