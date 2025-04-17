import numpy as np

arr = np.arange(10, 50)
print(f"Il primo array è di tipo {arr.dtype}")

arr_float = arr.astype(float)
print(f"Il secondo array è di tipo {arr_float}")

forma = np.shape(arr_float)
print(forma)

import numpy as np
import random

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
            print("1. Somma elemento per elemento dei due array")
            print("2. Somma totale degli elementi del nuovo array")
            print("3. Somma dei valori maggiori di 5 del nuovo array")
            print("0. Esci")

            scelta = input("Scegli un'opzione: ")

            match scelta:
                case "1":
                    calcolatore.somma_elementi()
                case "2":
                    calcolatore.somma_totale()
                case "3":
                    calcolatore.somma_maggiori_di_5()
                case "0":
                    print("Programma terminato.")
                    break
                case _:
                    print("Scelta non valida. Riprova.")

    # Primo menu per scegliere se inserire o generare casualmente i parametri
    def menu_iniziale():
        print("Benvenuto. Scegli come impostare i parametri:")
        print("1. Inserisci numero di elementi dell'array e i suoi valori estremi manualmente")
        print("2. Inserisci numero di elementi dell'array e i suoi valori estremi casualmente")

        scelta = input("Scelta: ")

        match scelta:
            case "1":
                tot = int(input("Numero di elementi dell'array: "))
                x = float(input("Valore iniziale: "))
                y = float(input("Valore finale: "))
            case "2":
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

        # Crea il calcolatore e subito i due array
        calcolatore = ArrayCalculator(tot, x, y)
        calcolatore.crea_array_linspace()
        calcolatore.crea_array_random()

        # Passa al menu delle operazioni
        menu_operazioni(calcolatore)

    # Avvio del programma
    menu_iniziale()

# Avvia la funzione principale
menu_es6()
