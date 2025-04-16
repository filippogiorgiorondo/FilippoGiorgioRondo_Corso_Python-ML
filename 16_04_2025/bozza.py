from abc import ABC, abstractmethod

# Classe astratta con ingredienti di base
class ModelloTorta(ABC):
    def __init__(self, nome, peso, ingredienti_aggiuntivi):
        # Gli ingredienti comuni sono sempre presenti
        self.nome = nome
        self.peso = peso
        self.ingredienti = ["farina", "zucchero", "uova"] + ingredienti_aggiuntivi

    @abstractmethod
    def calcola_prezzo(self):
        pass

# Sottoclasse per una Torta al cioccolato
class TortaCioccolato(ModelloTorta):
    def __init__(self, peso):
        super().__init__("Torta al Cioccolato", peso, ["cioccolato"])
        self.base_price = 15  # Prezzo base per la torta al cioccolato

    def calcola_prezzo(self):
        prezzo = self.base_price + (self.peso * 0.5)  # Il prezzo dipende dal peso
        return prezzo

# Sottoclasse per una Torta alla frutta
class TortaFrutta(ModelloTorta):
    def __init__(self, peso):
        super().__init__("Torta alla Frutta", peso, ["frutta"])
        self.base_price = 12  # Prezzo base per la torta alla frutta

    def calcola_prezzo(self):
        prezzo = self.base_price + (self.peso * 0.6)  # Il prezzo dipende dal peso
        return prezzo

# Sottoclasse per una Torta di mele
class TortaMela(ModelloTorta):
    def __init__(self, peso):
        super().__init__("Torta di Mela", peso, ["mele"])
        self.base_price = 10  # Prezzo base per la torta di mela

    def calcola_prezzo(self):
        prezzo = self.base_price + (self.peso * 0.4)  # Il prezzo dipende dal peso
        return prezzo
    
class Cliente():
    def __init__(self, nome, budget):
        self.nome = nome
        self.budget = budget

    # getter per visionare il budget
    def get_budget(self):
        return self.budget

    # Setter per visionare il budget
    def set_budget(self, budget):
        self.__budget = budget
        
    # prenota torta
    def prenota_torta(self, nome_torta):
        peso = float(input("Inserisci il peso"))