class Producte:

    def __init__(self, nom, preu, descompte):
        
        self.nom = nom
        self.preu = float(preu)
        self.descompte = float(descompte)

    def preuambdescompte(self):

        return float(self.preu*(1-self.descompte/100))
    
nom = input("Introdueix el nom del producte: ")
preu = float(input("Introdueix el preu del producte: "))
descompte = float(input("Introdueix el descompte que vulgui per el producte: "))

producte = Producte (nom, preu, descompte)

print(f"El producte {nom} te un preu de {preu} i amb el descompte et queda a {producte.preuambdescompte():.2f}")
        