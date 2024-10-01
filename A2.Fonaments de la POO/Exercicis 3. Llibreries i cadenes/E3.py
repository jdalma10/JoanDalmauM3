# 3. Escriu un programa que generi una hora específica a l'atzar (per exemple, les 10:30:00)
# i mostri quanta estona ha passat fins ara, en hores, minuts i segons.
from datetime import datetime
import random

# Generem una hora, minuts i segons aleatoris
hores = random.randint(0, 23)
minuts = random.randint(0, 59)
segons = random.randint(0, 59)

# Creem un objecte datetime amb l'hora aleatòria
hora_aleatoria = datetime.now().replace(hour=hores, minute=minuts, second=segons, microsecond=0)

# Obtenim l'hora actual
ara = datetime.now()

# Calculem la diferència en segons
diferencia = (ara - hora_aleatoria).total_seconds()

# Convertim la diferència a hores, minuts i segons
hores_passades = int(diferencia // 3600)
minuts_passats = int((diferencia % 3600) // 60)
segons_passats = int(diferencia % 60)

# Mostrem els resultats
print(f"Hora aleatòria generada: {hores:02}:{minuts:02}:{segons:02}")
print(f"Diferència fins ara: {hores_passades} hores, {minuts_passats} minuts i {segons_passats} segons.")
