try:
    numero = int(input("Ingresa un número: "))
    print(f"El número es: {numero}")
except ValueError:
    print("Error: Entrada inválida. Debes ingresar un número.")
