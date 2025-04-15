"""
creare una classe ContoBancario che incapsula le informazioni di un conto e
fornisce metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare
l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al
saldo del conto.



Classe ContoBancario:
Attributi privati:
__titolare (stringa che rappresenta il nome del titolare del conto)
__saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
deposita(importo): aggiunge un importo al saldo solo se l'importo è
positivo.
preleva(importo): sottrae un importo dal saldo solo se ci sono fondi
sufficienti e l'importo è positivo.
visualizza_saldo(): restituisce il saldo corrente senza permettere la sua
modifica diretta.
Gestione dei Metodi e Sicurezza:
I metodi deposita e preleva devono controllare che gli importi siano validi
(e.g., non negativi).
Aggiungere metodi "getter" e "setter" per gli attributi come _titolare,
applicando validazioni appropriate (e.g., il titolare deve essere una stringa
non vuota).
"""
class ContoBancario:
    def __init__(self, titolare, saldo):
        if type(titolare) == str and titolare.strip() == "": # verifica che il titolare non sia una stringa vuota
            raise ValueError("Il titolare deve essere una stringa non vuota.")
        if saldo < 0:
            raise ValueError("Il saldo iniziale non può essere negativo.")
        self.__titolare = titolare
        self.__saldo = saldo

    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, nuovo_titolare):
        if type(nuovo_titolare) == str and nuovo_titolare.strip() == "": # verifica che il nuovo titolare non sia una stringa vuota
            self.__titolare = nuovo_titolare
        else:
            raise ValueError("Il nuovo titolare deve essere una stringa non vuota.")

    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo}€ effettuato con successo.")
        else:
            print("L'importo deve essere maggiore di 0.")

    def preleva(self, importo):
        if importo <= 0:
            print("L'importo deve essere positivo.")
        elif importo > self.__saldo:
            print("Fondi insufficienti.")
        else:
            self.__saldo -= importo
            print(f"Prelievo di {importo}€ effettuato con successo.")

    def visualizza_saldo(self):
        print(f"Saldo disponibile: {self.__saldo}€")

# --- Menu con match-case ---
def menu_conto():
    nome = input("Inserisci il nome del titolare del conto: ")
    conto = ContoBancario(nome, 0.0)

    while True:
        print("\n--- MENU ---")
        print("1. Deposita")
        print("2. Preleva")
        print("3. Visualizza saldo")
        print("4. Cambia titolare")
        print("5. Esci")

        scelta = input("Scegli un'opzione (1-5): ")

        match scelta:
            case "1":
                try:
                    importo = float(input("Inserisci l'importo da depositare: "))
                    conto.deposita(importo)
                except ValueError:
                    print("Importo non valido.")
            case "2":
                try:
                    importo = float(input("Inserisci l'importo da prelevare: "))
                    conto.preleva(importo)
                except ValueError:
                    print("Importo non valido.")
            case "3":
                conto.visualizza_saldo()
            case "4":
                nuovo_titolare = input("Inserisci il nuovo nome del titolare: ")
                try:
                    conto.set_titolare(nuovo_titolare)
                    print("Titolare aggiornato con successo.")
                except ValueError as e:
                    print(f"Errore: {e}")
            case "5":
                print("Uscita dal programma. Grazie!")
                break
            case _:
                print("Scelta non valida. Riprova.")

# Esegui il menu
menu_conto()
