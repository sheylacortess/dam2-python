expresion = input("Escribe una expresión matemática: ")

try:
    resultado = eval(expresion)
    print("Resultado:", resultado)
except SyntaxError:
    print("Error: La expresión está mal escrita.")
except TypeError:
    print("Error: Se ha intentado una operación inválida (por ejemplo, combinar números y texto).")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except Exception as e:
    print(f"Ocurrió otro error inesperado: {e}")