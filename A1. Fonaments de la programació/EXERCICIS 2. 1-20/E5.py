#5. Escriure un programa que converteixi un valor donat en graus Fahrenheit a graus Celsius. Recordeu que la fórmula per a la conversió és:
# C = (F-32) * 5/9

grausF = float(input("Introdueix graus Farenheit: "))
grausC = (grausF - 32) * (5/9)
print (grausC)