def reserva(origen, destino, *viajeros, **detalles):
    print(f"Se ha reservado el vuelo de {origen} a {destino} para:")
    for viajero in viajeros:
        print(f"- {viajero}")

    print("Con los siguientes detalles:")
    for k in detalles:
        print(f"{k}: {detalles[k]}")

# Ejemplo de llamada:
reserva('Granada', 'México', 'Pedro', 'Juani', 'Lunoisa', comida='vegana', asientos='ventanilla', precio=350)