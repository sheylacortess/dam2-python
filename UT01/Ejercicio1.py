print("Mi coche gasta 5,5 litros cada 100 km y mi trabajo se encuentra a 15 kilómetros de casa. ¿Cuánto me gastaré en gasolina en 20 días laborables si el precio es de 1,12 €/l?")
gasto = 5.5
distancia = 15
dias = 20 
precio = 1.12

gastoIda = ((gasto/100)*15)* 1.12
print ("El gasto de la ida diario es de ", gastoIda, "€")

gastoTotal = (gastoIda * 40)
print("El gasto total en 20 días ida y vuelta es de ", gastoTotal, "€")


## los decimales en python se ponen con el punto 