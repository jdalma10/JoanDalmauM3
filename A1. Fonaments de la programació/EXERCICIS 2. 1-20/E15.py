var1 = 10
var2 = 20
print (f"1: {var1}, 2:{var2}")

#necessiem una variable auxiliar per a fer l'intercanvi
aux = var2
var2 = var1
var1 = aux
print("Intercanvi")
print (f"1: {var1}, 2:{var2}")