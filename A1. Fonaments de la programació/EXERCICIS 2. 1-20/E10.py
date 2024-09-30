
parcialA = int(input("Nota del parcialA: "))
parcialB = int(input("Nota del parcialB: "))
parcialC = int(input("Nota del parcialC: "))

examenFinal = int(input("Nota del examen final: "))

treballFinal = int(input("Nota del treball final: "))

nParcials = (parcialA + parcialB + parcialC) / 3

total = (nParcials * 0.30) + (examenFinal * 0.55) + (treballFinal * 0.15)

print(f"La nota final es de: {total}")