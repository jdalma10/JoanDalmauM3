# 7. Realitza un programa que rebi una quantitat de minuts i mostri per pantalla a quantes hores i minuts correspon.
# Per exemple: 1000 minuts són 16 hores i 40 minuts.

qMinuts = int(input("Quantitat de minuts: "))

hores = qMinuts // 60
minuts = qMinuts % 60

print(f"{qMinuts} son {hores} hores i {minuts}minuts")