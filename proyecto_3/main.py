# Separador

separador = "*"*80
titulo = "**ANALIZADOR DE TEXTOS**"

# Captura de la informaci
#  Encabezado
print(separador)
print(titulo.center(80, " "))
print(separador)

# Captura del texto por el usuario.
print(separador)
texto = input("Ingresa un texto: ")
print(separador)
# print(texto)

# Captura de letras por el usuario.
print(separador)
print("Ingresa tres letras de tu eleccion: ")

a = input("Primera letra: ")
b = input("Segunda letra: ")
c = input("Tercera letra: ")
print(separador)

# convertir los datos en minusculas

texto = texto.lower()
a = a.lower()
b = b.lower()
c = c.lower()

resultado = texto.split()
# print(resultado)

# print(texto)
# print(a)
# print(b)
# print(c)

# alacenamos las letras en una lista

lista = [a, b, c]
# print(lista)
# Primero

print(separador)
print(f'La letra {a} aparece en el texto: {
      texto.count(a)} de veces en el texto introducido')
print(f'La letra {b} aparece en el texto: {
      texto.count(b)} de veces en el texto introducido')
print(f'La letra {c} aparece en el texto: {
      texto.count(c)} de veces en el texto introducido')
print(separador)
# Segundo
print(separador)
print(f'El texto continen {len(resultado)} palabras.')
print(separador)

# Tercero
print(separador)
print(f'La primera letra del texto es: {texto[0]}')
print(f'La ultima letra del texto es: {texto[-1]}')
print(separador)

# Cuarta
print(separador)
print(f'Si se invierte en orden de las palabras quedaria: {
      " ".join(resultado[::-1])}')
print(separador)

# Quinta
print(separador)
control = 'python' in resultado
dic = {True: 'Si aparece la palabra de "Python" en el texto',
       False: 'No aparce la palabra de "Python" en el texto'}
print(f" {dic[control]}")
print(separador)
