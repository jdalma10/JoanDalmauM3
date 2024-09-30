#8. Un venedor rep un sou base més un 10% extra per comissió de les seves vendes, el venedor vol saber quants diners obtindrà per concepte de comissions per les tres vendes que realitza en el mes i el total que rebrà al mes tenint en compte el seu sou base i comissions.

venta1 = float(input("Venta 1: "))
venta2 = float(input("Venta 2: "))
venta3 = float(input("Venta 3: "))
souBase = float(input("Sou base: "))

comisio = (venta1 + venta2 + venta3) * 0.1

# En un string podem conatenar no només variables sin´també exressions
print(f"Cobraràs {souBase + comisio} euros")
