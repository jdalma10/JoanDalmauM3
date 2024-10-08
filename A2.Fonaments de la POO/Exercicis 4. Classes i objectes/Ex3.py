class Persona:
    def __init__(self, pNom, pEdat):
        self.nom = pNom
        self.edat = pEdat
    
    def __str__(self):
        return self.nom + ": " + str(self.edat)

    def presenta(self):
        return f"Hola em dic {self.nom} i tinc {self.edat}."
    
    
        




presona1 = Persona("Joan", 38)

print(presona1.presenta())