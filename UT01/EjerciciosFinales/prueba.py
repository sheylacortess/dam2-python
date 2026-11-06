def procesar_calificaciones(nombre_alumno, *notas, **kwargs):
    print(f"Alumno: {nombre_alumno}")
    
    # Calcular la media si hay notas
    if notas:
        media = sum(notas) / len(notas)
        print(f"Nota media: {media:.2f}")
    else:
        print("No se han proporcionado notas.")
        
    # Comprobar si en los kwargs viene la orden de imprimir detalles
    if kwargs.get("imprimir_detalles") == True:
        print("--- Detalles adicionales ---")
        for clave, valor in kwargs.items():
            if clave != "imprimir_detalles":  # Omitimos el interruptor
                print(f"{clave}: {valor}")

# Ejemplo de llamada de prueba:
procesar_calificaciones("Carlos", 7, 8, 9, 10, asignatura="Matemáticas", convocatoria="Ordinaria", imprimir_detalles=True)