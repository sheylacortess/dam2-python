print("Prueba1")
print("")
# verificacion de identidad de listas
lista1 = [1,2,3]
lista2 = [1,2,3]
lista3 = lista1
son_iguales = (lista1 is lista2) # false ya que no son el mismo objeto aunque contengan los mismos numeros 
son_iguales2 = (lista1 is lista3) #true ya que son el mismo objeto
print("Lista 1 y 2 son iguales en el espacio de memoria: ", son_iguales)
print("Lista 1 ty 3 son iguales en el espacio de memoria: ", son_iguales2)

#comprobacion 2
print("")
son_iguales3 = (lista1 == lista2)
print("Lista 1 y 2 son iguales? (los nuemeros que contiene)", son_iguales3)

## OPERADORES DE PERTENENCIA 
# operador IN y NOT IN

print("")
frutas = ["manzana", "banana", "cereza"]
es_banana = "banana" in frutas #true
no_es_uva = "uva" in frutas # false 
print ("La lista es: ", frutas)
print ("Bananna esta en la lista? ", es_banana)
print("Uva esta en la lista? ", no_es_uva)


## Variables y Tipos de Datos --> memoria del ordenador 
print("")
a = 5
id(a)
print(id(a))
print (a.bit_length())


## repasar puertas logicas y operadores de desplazamiento (página 22 del pdf sintaxisBasicaPython)
## importante la págian 36 