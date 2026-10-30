#El programa pide un número entero positivo n y cuenta desde 1 hasta n.
# Si el usuario introduce algo que no sea entero o menor que 1, se pide de nuevo.
# Si se interrumpe con Ctrl + C, el programa se despide limpiamente.

print("Contador con control de errores --> Ctrl + C")
try:
    while True: 
        try: 
            entrada = int(input("Introduzca un numeor positvo: "))
            if entrada < 1:
                print("El número tiene que ser mayor o igual que 1.")
                continue

        except ValueError:
            print("Debes introducir un numero válido")
            continue
        print("Contando del 1 al {entrada}")
        for i in range (1, entrada +1 ):
            print(i, end= " ")
        print("Terminado")
except KeyboardInterrupt:
    print("\nGracias por jugar 😶‍🌫️")
        
