import random

class Lanzar:
    @staticmethod
    def lanzamiento():
        return random.randint(1,6)
    
lanzamiento1 = Lanzar.lanzamiento()
lanzamiento2 = Lanzar.lanzamiento()
lanzamiento3 = Lanzar.lanzamiento()
lanzamiento4 = Lanzar.lanzamiento()

print(f"{lanzamiento1}-{lanzamiento2}-{lanzamiento3}-{lanzamiento4}")