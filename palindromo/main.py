# Se soliicta al usuario que ingrese la palabra o texto
palabra = input('Inserta la palabra o el texto: ')

# Se eliminan espacion y se convierte odo el texto en minusculas
palabra = palabra.lower().replace(' ', '')

# Se compara la palabra o texto con su reverso y arroja si cumple o no
if palabra == palabra[::-1]:
    print("Es un palindromo")
else:
    print("No es un palindromo")
