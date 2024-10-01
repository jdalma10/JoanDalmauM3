# 2. Escriu un programa que generi tres números aleatoris entre 1 i 100,
# els mostri i després en mostri la seva suma.
import random

num1 = random.randint(1,100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(f"Els tres números aleatoris són: {num1}, {num2}, {num3}")
print(f"La suma és: {num1 + num2 + num3}")
