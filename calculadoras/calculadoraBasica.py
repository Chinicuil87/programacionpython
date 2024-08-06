# Imprime el titulo de aplicacion
print("*"*50)
print(" "*16 + "Calculadora Basica")
print("*"*50)

# Solicita los numeros al usuario
numeroUno = int(input("Ingresa el primer valor: "))
numeroDos = int(input("Ingresa el segundo numero: "))

# Operaciones basicas
suma = numeroUno + numeroDos
resta = numeroUno - numeroDos
multi = numeroUno * numeroDos
div = numeroUno / numeroDos

# Imprime los resultados del las operaciones.
print("*"*50)
print(f"""
La suma de los numeros {numeroUno} + {numeroDos} es: {suma}
La resta de los numeros {numeroUno} - {numeroDos} es: {resta}
La multiplicacion de los numeros {numeroUno} * {numeroDos} es: {multi}
La division de los numeros {numeroUno} / {numeroDos} es: {div}
""")

print("*"*50)
