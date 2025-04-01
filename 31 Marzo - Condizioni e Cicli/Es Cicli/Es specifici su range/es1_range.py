# Chiede all'utente cosa fare
whatdo = input("Benvenuto nel programma 'pari o dispari'. Digitare 1 se interessato ad un numero intero, digitare 2 se interessato ad una stringa: ")
match whatdo:
    case "1": # Caso in cui verificare un numero intero
        numero = int(input("Inserire il numero da verificare: "))
        if numero % 2 == 0: # Se il resto della divisione per 2 è nullo, allora è pari
            print("Il numero inserito è pari")
        else: # Se non è verificata la condizione precedente, il numero è dispari
            print("Il numero inserito è dispari")

    case "2": # Caso in cui verificare una stringa
        stringa = input("Inserisci qui la tua stringa (non accettati gli spazi): ").lower()
        if len(stringa) % 2 == 0: # Se il resto della divisione per 2 è nullo, allora è pari il numero di char di cui è composta
            print("La tua stringa è pari (è costituita da un numero pari di char)")
        else: # Se non è verificata la condizione precedente, il numero è dispari il numero di char di cui è composta
            print("La tua stringa è dispari (è costituita da un numero dispari di char)")
    
    case _: # Caso di default che si verifica se le condizioni precedenti non sono soddisfatte
        print("Operazione non riconosciuta")
