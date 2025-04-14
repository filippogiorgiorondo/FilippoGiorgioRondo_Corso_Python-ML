class Animale:
    def __init__(self, nome, peso, verso):
        self.nome = nome
        self.peso = peso
        self.verso = verso
    
    def fai_suono(self):
        print("L'animale fa un suono.")

class Coccodrillo(Animale):
    def __init__(self, nome, peso, verso):
        super().__init__(nome, peso, verso)
        
    def fai_suono(self):
        print(f"Che verso fa il coccodrillo non si sa: {self.verso}")
        
    def attivita(self):
        print("Il coccodrillo nuota nel lago")
        
class Zebra(Animale):
    def __init__(self, nome, peso, verso):
        super().__init__(nome, peso, verso)
        
    def fai_suono(self):
        print(f"La zebra nitrisce:{self.verso}")
        
    def attivita(self):
        print("La zebra sta scappando da una iena")

class Iena(Animale):
    def __init__(self, nome, peso, verso):
        super().__init__(nome, peso, verso)
        
    def fai_suono(self):
        print(f"La iena ringhia: {self.verso}")
        
    def attivita(self):
        print("La iena sta cacciando la zebra")

cocco = Coccodrillo("Crocky", 300, "BOOOH")
zebra = Zebra("Zebrina", 220, "HIIIII")
iena = Iena("Ieny", 180, "GRRRR")

animali = [cocco, zebra, iena]

for animale in animali:
    print(f"--- {animale.nome} ---")
    animale.fai_suono()
    animale.attivita()
    print()

