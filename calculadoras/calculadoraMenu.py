print("*"*50)
print(" "*19 + "CALCULADORA")
print("*"*50)

menu = """
        Menu
        
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
    
"""
resultado = " "
continuar = True

while continuar:
    print(menu)
    opcion = int(input("Selecciona una opcion:  "))
    if opcion == 1:
        print("Suma")
    elif opcion == 2:
        print("Resta")
    elif opcion == 3:
        print("Multiplicacion")
    elif opcion == 4:
        print("Division")
    elif opcion == 5:
        print("Saliendo del programa")
        continuar = False
        break
    else:
        print("opcion no valida")
