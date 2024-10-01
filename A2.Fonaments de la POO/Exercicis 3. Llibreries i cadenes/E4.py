# 4. Escriu un programa que generi cinc números decimals aleatoris entre 0 i 1,
# i els mostri en la mateixa línia, separats per guions, no es poden utilitzar llistes.
import random

# Generem cinc números decimals aleatoris
num1 = random.randint(1,9)*0.1
num2 = random.random()
num3 = random.random()
num4 = random.random()
num5 = random.random()

# Mostrem els números separats per guions
print(f"{num1} - {num2} - {num3} - {num4} - {num5}")
# Mostrem els números separats per guions utilitzant sep
print(num1, num2, num3, num4, num5, sep=' - ')