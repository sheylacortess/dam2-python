
print("Calculadora Segura")
print("Escribe 'salir' en cualquier momento para terminar.")

while True:
    entrada_x = input("Introduce el primer número (o 'salir'): ")
    if entrada_x.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    try:
        x = float(entrada_x)
    except ValueError:
        print(" Error: Debes introducir un valor numérico válido.\n")
        continue

    operador = input("¿Qué quieres hacer (+, -, *, /): ")
    if operador.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    if operador not in ["+", "-", "*", "/"]:
        print(" Error: Operador no válido. Usa +, -, * o /.\n")
        continue

    entrada_y = input("Introduce el segundo número (o 'salir'): ")
    if entrada_y.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    try:
        y = float(entrada_y)
    except ValueError:
        print(" Error: Debes introducir un valor numérico válido.\n")
        continue

    resultado = None
    if operador == "+":
        resultado = x + y
    elif operador == "-":
        resultado = x - y
    elif operador == "*":
        resultado = x * y
    elif operador == "/":
        try:
            resultado = x / y
        except ZeroDivisionError:
            print(" Error: No es posible realizar una división entre 0.\n")
            continue

    # Mostrar resultado si todo ha ido bien
    print(f" Resultado: {x} {operador} {y} = {resultado}\n")