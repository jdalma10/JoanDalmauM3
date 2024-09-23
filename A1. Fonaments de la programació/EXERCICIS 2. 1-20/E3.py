import math

catetA = int(input("Dona el primer catet: "))
catetB = int(input("Dona el segon catet: "))

hipotenusa = math.sqrt((catetA *2) + (catetB * 2))
#hipotenusa = ((catetA **2) + (catetB ** 2))** 0.5

print(f"La hipotenusa es: {hipotenusa}")

# userInput = input("Introdueix els 2 catets separats per una coma")
# catetA = int(userInput.split(',')[0])
# catetB = int(userInput.split(',')[1])