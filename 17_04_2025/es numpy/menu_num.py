import numpy as np
import random
import lista_es_num as len # modulo contenente tutti gli esercizi su numpy


def menu_es6():
    print("==== BENVENUTO NEL MENU DELL'ESERCIZIO 6 ====")
    # Classe che gestisce la creazione e manipolazione di array
    class ArrayCalculator:
        def __init__(self, tot=0, x=0, y=0):
            self.tot = tot
            self.x = x
            self.y = y
            self.array_linspace = None
            self.array_random = None
            self.array_somma = None

        # Crea un array equidistante tra x e y
        def crea_array_linspace(self):
            self.array_linspace = np.linspace(self.x, self.y, self.tot)
            print(f"\nArray equidistante tra {self.x} e {self.y}:\n{self.array_linspace}")

        # Crea un array di numeri casuali tra 0 e 1
        def crea_array_random(self):
            self.array_random = np.random.random(self.tot)
            print(f"\nArray di numeri casuali tra 0 e 1:\n{self.array_random}")

        # Somma gli elementi dei due array posizione per posizione
        def somma_elementi(self):
            if self.array_linspace is None or self.array_random is None:
                print("Devi prima creare entrambi gli array.")
                return
            self.array_somma = self.array_linspace + self.array_random
            print(f"\nSomma elemento per elemento:\n{self.array_somma}")

        # Calcola la somma totale del nuovo array
        def somma_totale(self):
            if self.array_somma is None:
                print("Devi prima sommare gli array.")
                return
            somma = np.sum(self.array_somma)
            print(f"\nSomma totale del nuovo array: {somma}")

        # Calcola la somma degli elementi del nuovo array maggiori di 5
        def somma_maggiori_di_5(self):
            if self.array_somma is None:
                print("Devi prima sommare gli array.")
                return
            somma_filtrata = np.sum(self.array_somma[self.array_somma > 5])
            print(f"\nSomma degli elementi maggiori di 5: {somma_filtrata}")


    # Mostra il menu delle operazioni
    def menu_operazioni(calcolatore):
        while True:
            print("\n--- MENU OPERAZIONI ---")
            print("1. Crea array con np.linspace")
            print("2. Crea array con np.random.random")
            print("3. Somma elemento per elemento dei due array")
            print("4. Somma totale degli elementi dei due array")
            print("5. Somma dei valori maggiori di 5 della somma degli elementi dei due array")
            print("0. Esci")

            scelta = input("Scegli un'opzione: ")

            # Gestione delle opzioni con match-case
            match scelta:
                case "1":
                    calcolatore.crea_array_linspace()
                case "2":
                    calcolatore.crea_array_random()
                case "3":
                    calcolatore.somma_elementi()
                case "4":
                    calcolatore.somma_totale()
                case "5":
                    calcolatore.somma_maggiori_di_5()
                case "0":
                    print("Programma terminato.")
                    break
                case _:
                    print("Scelta non valida. Riprova.")


    # Primo menu per scegliere se inserire o generare casualmente i parametri
    def menu_iniziale():
        print("Benvenuto. Scegli come impostare i parametri:")
        print("1. Inserisci TOT, x e y manualmente")
        print("2. Genera TOT, x e y casualmente")

        scelta = input("Scelta: ")

        # Gestione scelta dell’utente
        match scelta:
            case "1":
                tot = int(input("Numero di elementi (TOT): "))
                x = float(input("Valore iniziale x: "))
                y = float(input("Valore finale y: "))
            case "2":
                # Generazione casuale dei parametri
                tot = random.randint(5, 100)
                x = round(random.uniform(0, 50), 2)
                y = round(random.uniform(x + 1, x + 50), 2)
                print("\nParametri generati casualmente:")
                print(f"TOT = {tot}")
                print(f"x = {x}")
                print(f"y = {y}")
            case _:
                print("Scelta non valida. Riprova.\n")
                return menu_iniziale()

        # Crea l'oggetto calcolatore e avvia il menu operazioni
        calcolatore = ArrayCalculator(tot, x, y)
        menu_operazioni(calcolatore)


    # Punto di ingresso del programma
    menu_iniziale()

