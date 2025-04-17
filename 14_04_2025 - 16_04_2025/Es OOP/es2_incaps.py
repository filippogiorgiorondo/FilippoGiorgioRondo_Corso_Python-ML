"""Sistema di gestione studenti

Immagina di dover creare un sistema di gestione per una scuola che deve mantenere le informazioni sugli studenti, i professori e le
lezioni. Seguendo il paradigma della programmazione orientata agli oggetti (OOP), dovrai implementare le classi necessarie usando
incapsulamento, ereditarietà e polimorfismo.
Specifiche

Classe Persona:
Crea una classe base chiamata Persona che rappresenti una persona generica.
Attributi:
nome: stringa
eta: intero
Metodi:
__init__(self, nome, eta): costruttore che inizializza nome ed eta.
presentazione(self): metodo che stampa una frase con il nome e l'età della persona.
Regola 1 - Incapsulamento: Gli attributi nome ed eta devono essere privati. Usa getter e setter per accedere e modificare il
nome e l'età.
Classe Studente:
Crea una sottoclasse di Persona chiamata Studente.
Attributi:
voti: lista di interi che rappresentano i voti dello studente.
Metodi:
__init__(self, nome, eta, voti): costruttore che inizializza il nome, l'età e i voti dello studente.
calcola_media(self): metodo che restituisce la media dei voti.
Override del metodo presentazione(self) per includere la media dei voti nella presentazione.
Regola 2 - Ereditarietà: Studente eredita dalla classe Persona.
Classe Professore:
Crea una sottoclasse di Persona chiamata Professore.
Attributi:
materia: stringa che rappresenta la materia insegnata.
Metodi:
__init__(self, nome, eta, materia): costruttore che inizializza il nome, l'età e la materia insegnata dal professore.
Override del metodo presentazione(self) per includere la materia nella presentazione."""

class Scuola:
    def __init__(self, nome):
        self.nome = nome
        self.studenti = []
        self.professori = []

    def crea_studente(self, nome, eta, voti=None):
        studente = Studente(nome, eta, voti)
        self.studenti.append(studente)
        return studente

    def crea_professore(self, nome, materia):
        professore = Professore(nome, materia)
        self.professori.append(professore)
        return professore

    def elenco_studenti(self):
        return [s.nome for s in self.studenti]

    def elenco_professori(self):
        return [p.nome for p in self.professori]

# verifica dell'input non nella class
class Persona:
    def __init__(self, nome, eta):
        if type(nome) != str and nome.strip() == "": # verifica che il nome non sia una stringa vuota
            raise ValueError("Il nome deve essere una stringa non vuota.")
        if type(eta) != int:
            raise ValueError("L'età deve essere un numero intero")
        self.__nome = nome
        self.__eta = eta
    def presentazione(self):
        print(f"Ciao, sono {self.nome} e ho {self.eta} anni")

# verificare che i voti siano una lista di interi
    
class Studente(Persona):
    def __init__(self, nome, eta, lista_voti):
        super().__init__(nome, eta)
        self.__lista_voti = lista_voti
        self.__media_voti = 0
        
    def calcola_media(self):
        self.__media_voti = sum(self.__lista_voti) / len(self.__lista_voti) if len(self.__lista_voti) < 0 else 0
    
    def presentazione(self):
        print(f"Ciao mi chiamo {self.__nome}, ho {self.__eta} e la mia media di voti è {self.__media_voti}")
    
class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia
    
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.__nome}, ho {self.__eta}, sono un prof di {self.__materia}")