# 12. Demana a l'usuari dos parells de nombres x1, y1 i x2, y2, que representin dos punts en el pla. Calcula i mostra la distància entre ells.
x1 = int(input("X 1: "))
y1 = int(input("Y 1: "))

x2 = int(input("X 2: "))
y2 = int(input("Y 2: "))


# Calculem els catets
c1 = abs(x2 - x1)
c2 = abs(y2 - y1)

# Calculem hipotenusa
h = (c1**2 + c2**2)**0.5
print(h)
