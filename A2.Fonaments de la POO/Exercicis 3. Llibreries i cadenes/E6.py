# 6. Escriu un programa que generi una cadena de 3 caràcters que inclogui lletres (majúscules i minúscules)
# i números aleatoris.
import random
import string

# Creem un conjunt de caràcters que inclou lletres i dígits
caracters = string.ascii_letters + string.digits

# Generem una cadena aleatòria de 8 caràcters
caracter1 = random.choice(caracters)
caracter2 = random.choice(caracters)
caracter3 = random.choice(caracters)


# Unim tots els caràcters en una cadena
cadena_aleatoria = caracter1 + caracter2 + caracter3 

# Mostrem la cadena generada
print(f"Cadena aleatòria: {cadena_aleatoria}")
