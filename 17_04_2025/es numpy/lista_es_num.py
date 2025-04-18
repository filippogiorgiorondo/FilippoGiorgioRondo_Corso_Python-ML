import numpy as np
import random


def menu_es4():
    print("==== BENVENUTO NEL MENU DELL'ESERCIZIO 4 ====")
    def menu():
        print("\nPer generare il tuo array, inserisci:")
        inizio = int(input("  ▶ Inizio: "))
        fine = int(input("  ▶ Fine: "))
        step = int(input("  ▶ Passo: "))

        if step == 0:
            print("Lo step non può essere 0. Impostato a 1.")
            step = 1

        if (fine > inizio and step < 0) or (fine < inizio and step > 0):
            print("Direzione incompatibile. Inverto il segno dello step.")
            step = -step

        return np.arange(inizio, fine, step)

    def aggiungi_riga():
        print("-- Benvenuto nella generazione di array NumPy --")
        righe = []

        scelta = input("Vuoi creare un array con una sola riga o più righe? (1 per una riga, 2 per più righe): ")

        if scelta == "1":
            righe.append(menu())

        elif scelta == "2":
            print("\nPuoi aggiungere più righe. Per terminare, digita 'n' quando ti viene chiesto se vuoi continuare.")

            prima_riga = menu()
            righe.append(prima_riga)

            while True:
                # Prima chiedi se vuole continuare
                scelta_continua = input("Vuoi continuare ad aggiungere righe? (s per sì, n per no): ").lower()
                if scelta_continua != "s":
                    break

                nuova_riga = menu()

                if len(nuova_riga) != len(prima_riga):
                    print("La nuova riga deve avere lo stesso numero di elementi della prima riga!")
                    continue

                righe.append(nuova_riga)
                print(f"RIGA AGGIUNTA: {nuova_riga}")
        else:
            print("Scelta non valida!")
            return

        array_totale = np.array(righe)
        print("\nArray finale generato:")
        print(array_totale)

    aggiungi_riga()

def menu_es5():
    print("==== BENVENUTO NEL MENU DELL'ESERCIZIO 5 ====")
    def mostra_array():
        arr = np.linspace(0, 1, 12)
        print(f"\n▶ Array (12 valori equidistanti tra 0 e 1):\n{arr}")

    def mostra_matrice():
        arr = np.linspace(0, 1, 12)
        matrice = arr.reshape(3, 4)
        print(f"\n▶ Matrice 3x4 ricavata dall'array:\n{matrice}")

    def somma_elementi_array():
        arr = np.linspace(0, 1, 12)
        somma = arr.sum()
        print(f"\n▶ Somma degli elementi dell'array originale: {somma}")

    def somma_due_matrici():
        matrice1 = np.array([[1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12]])

        matrice2 = np.array([[2, 4, 6, 8],
                            [1, 3, 5, 7],
                            [0, 1, 0, 1]])

        print("\n▶ Matrice 1:")
        print(matrice1)
        print("\n▶ Matrice 2:")
        print(matrice2)

        somma1 = np.sum(matrice1)
        somma2 = np.sum(matrice2)
        somma_totale = somma1 + somma2

        print(f"\n▶ Somma degli elementi della matrice 1: {somma1}")
        print(f"▶ Somma degli elementi della matrice 2: {somma2}")
        print(f"▶ Somma totale delle due matrici: {somma_totale}")

    # --- MENU ---
    def menu():
        while True:
            print("\n--- MENU ---")
            print("1. Mostra array di 12 numeri equidistanti tra 0 e 1")
            print("2. Mostra la matrice 3x4 ricavata dall'array")
            print("3. Mostra la somma degli elementi dell'array originale")
            print("4. Mostra la somma totale di due matrici esempio")
            print("0. Esci")

            scelta = input("Scegli un'opzione: ")

            match scelta:
                case "1":
                    mostra_array()
                case "2":
                    mostra_matrice()
                case "3":
                    somma_elementi_array()
                case "4":
                    somma_due_matrici()
                case "0":
                    print("Uscita dal programma.")
                    break
                case _:
                    print("Scelta non valida. Riprova!")
    menu()
    
def menu_es6():

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
            print("Specificare come creare il secondo array")
            print("1. Manualmente (con np.linspace)")
            print("2. Casualmente (con np.random.random)")
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
        print("==== BENVENUTO NEL MENU DELL'ESERCIZIO 6 ====")
        print("Scegli come impostare i parametri per la creazione del primo array:")
        print("1. Manualmente (con np.linspace)")
        print("2. Casualmente (con np.random.random)")
        
        scelta = input("Scelta: ")

        # Gestione scelta dell’utente
        match scelta:
            case "1":
                tot = int(input("Numero di elementi: "))
                x = float(input("Valore iniziale: "))
                y = float(input("Valore finale: "))
            case "2":
                # Generazione casuale dei parametri
                tot = random.randint(5, 100)
                x = round(random.uniform(0, 50), 2)
                y = round(random.uniform(x + 1, x + 50), 2)
                print("\nParametri generati casualmente:")
                print(f"Numero elementi = {tot}")
                print(f"Valore iniziale = {x}")
                print(f"Valore finale = {y}")
            case _:
                print("Scelta non valida. Riprova.\n")
                return menu_iniziale()

        # Crea l'oggetto calcolatore e avvia il menu operazioni
        calcolatore = ArrayCalculator(tot, x, y)
        menu_operazioni(calcolatore)


    # Punto di ingresso del programma
    menu_iniziale()
menu_es6()