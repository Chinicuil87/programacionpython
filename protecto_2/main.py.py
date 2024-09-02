
# Variables
separador = "*"*100
print(separador)
nombre = input("Nombre del vendedor: ")
total_ventas = float(input("Tatal de lo vendido del mes: "))

# Operacion
comision = round(total_ventas * 0.13, 2)
# Resultado en pantalla
print(separador)
print(f'El vendedor {nombre}, vendio un total en el mes de {
      total_ventas} por lo cual le toca una comision de {comision}')
print(separador)
