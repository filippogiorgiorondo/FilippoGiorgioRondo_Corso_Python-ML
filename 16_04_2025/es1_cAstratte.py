from abc import ABC, abstractmethod

# Classe astratta
class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base

    @abstractmethod
    def calcola_stipendio(self):
        pass

# Classe derivata - Impiegato fisso
class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        return self.stipendio_base

# Classe derivata - Impiegato a provvigione
class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite, percentuale_bonus):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite
        self.percentuale_bonus = percentuale_bonus  # Esempio: 0.1 per 10%

    def calcola_stipendio(self):
        bonus = self.vendite * self.percentuale_bonus
        return self.stipendio_base + bonus

# Funzione per stampare le info
def stampa_info_impiegato(impiegato):
    print(f"Nome: {impiegato.nome} {impiegato.cognome}")
    print(f"Stipendio calcolato: €{impiegato.calcola_stipendio():.2f}")
    print("-" * 30)

# Esempio di utilizzo
if __name__ == "__main__":
    imp1 = ImpiegatoFisso("Luca", "Rossi", 2000)
    imp2 = ImpiegatoAProvvigione("Anna", "Bianchi", 1500, vendite=10000, percentuale_bonus=0.05)

    stampa_info_impiegato(imp1)
    stampa_info_impiegato(imp2)
