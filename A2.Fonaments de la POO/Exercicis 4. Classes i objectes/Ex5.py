#5. Crea una classe Cercle amb un atribut radi. 
# Afegeix un mètode que calculi l'àrea del cercle.
#  Demana a l'usuari que introdueixi
#  el radi i mostra l'àrea.
#

userNum = int(input("Digam un radi: "))

class Cercle:
    def __init__(self, radi):
        self.radi = radi
    
    def circul (self):
        return 3.14 * self.radi ** 2
    
    
circul1 = Cercle(userNum)

print(circul1.circul())
        