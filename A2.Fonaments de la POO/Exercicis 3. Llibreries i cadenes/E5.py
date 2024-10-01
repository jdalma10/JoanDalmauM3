# 5. Escriu un programa que demani a l'usuari una cadena i mostri el primer i l'últim caràcter,
# els dos en majúscules.
cadena = input("Introdueix una cadena: ")

# Obtenim el primer i l'últim caràcter
primer = cadena[0].upper()
ultim = cadena[-1].upper()

# Mostrem els caràcters en majúscules
print(f"El primer caràcter en majúscules és: {primer}")
print(f"L'últim caràcter en majúscules és: {ultim}")
