# 8. Escriu un programa que generi un color aleatori en format RGB.
# Cada component (R, G, B) ha de ser un valor entre 0 i 255.
import random

# Generem valors aleatoris per cada component de color
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

# Mostrem el color generat
print(f"El color RGB generat és: ({r}, {g}, {b})")
