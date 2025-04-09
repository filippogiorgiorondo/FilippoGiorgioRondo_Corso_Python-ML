from random import randint

numeri = [randint(1, 10) for _ in range(5)]

def scrittura(stringa, metodo):
    percorso = r"C:\Users\filip\Documents\GitHub\FilippoGiorgioRondo_Corso_Python-ML\7-8 Aprile - Esercitazione\Esercizi\prova.txt"
    
    # Preparo tutte le righe in una sola stringa
    righe = '\n'.join([stringa for _ in numeri]) + '\n'
    
    # Apro il file una sola volta
    with open(percorso, metodo) as file:
        file.write(righe)

percorso = r"C:\Users\filip\Documents\GitHub\FilippoGiorgioRondo_Corso_Python-ML\7-8 Aprile - Esercitazione\Esercizi\prova.txt"

with open(percorso, "r") as file:
    numeri = file.readlines()

scrittura("ciao", "w")


