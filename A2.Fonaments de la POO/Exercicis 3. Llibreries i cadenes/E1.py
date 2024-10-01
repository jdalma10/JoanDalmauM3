from datetime import datetime

data1_str = input("Introdueix la primera data (YYYY-MM-DD): ")
data2_str = input("Introdueix la segona data (YYYY-MM-DD): ")

# Convertim les dates de cadena a objecte datetime
data1 = datetime.strptime(data1_str, "%Y-%m-%d")
data2 = datetime.strptime(data2_str, "%Y-%m-%d")

# Calculem la diferència en dies
diferencia = abs((data2 - data1).days)
print(f"La diferència entre les dues dates és de {diferencia} dies.")
