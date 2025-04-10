import random

def genera_numero():
    #genera un numero casuale da 1 a 100 inclusi
    return random.randint(1, 100)

def minore_o_maggiore(numero, guess):
    #verifica che l'input utente sia maggiore, minore o uguale al numero da indovinare
    if guess > numero:
        print("Il tuo numero è minore del numero da indovinare")
        return False
    elif guess < numero:
        print("Il tuo numero è maggiore del numero da indovinare")
        return False
    else:
        print("Complimenti, hai indovinato!")
        return True

def gioco():
    # Funzione di gioco
    guess = genera_numero()
    condizione = True

    while condizione:
        numero = input("Inserisci il numero da indovinare: ")
        
        if not numero.isdigit():  # Controlla che l'input sia un numero
            print("Inserisci un numero valido!")
            continue
        
        numero = int(numero)
        condizione = not minore_o_maggiore(numero, guess)  # Se l'utente indovina, `condizione` diventa False

        if not condizione:  # Esce dal ciclo se l'utente ha indovinato
            break

        whatdo = input("Vuoi ritentare (1) o concludere il programma (2)?: ")
        
        if whatdo == "2":
            print("Grazie per aver giocato!")
            break
        elif whatdo != "1":
            print("Scelta non valida, riprova.")

# Avvia il gioco
gioco()
