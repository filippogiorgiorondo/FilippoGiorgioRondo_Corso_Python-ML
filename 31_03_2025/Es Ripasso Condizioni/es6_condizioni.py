# Chiede all'utente di inserire il primo numero
n1 = int(input("Benvenuto. Qui potrai eseguire operazioni tra due numeri\nInserisci il primo numero: "))

# Chiede all'utente di inserire il secondo numero
n2 = int(input("Perfetto, inserisci il secondo numero: "))

# Chiede all'utente di scegliere un'operazione
operazione = input("Scegliere un'operazione disponibile tra le seguenti:\nSomma(1)\nSottrazione(2)\nMoltiplicazione(3)\nDivisione(4)\nPotenza(5)")

# Inizia un match per decidere quale operazione eseguire
match operazione:
    # Caso per la somma
    case "1":
        risultato = n1 + n2  # Somma dei due numeri
        print(f"{risultato}, è il risultato")  # Stampa il risultato della somma

    # Caso per la sottrazione
    case "2":
        risultato = n1 - n2  # Sottrazione del secondo numero dal primo
        print(f"{risultato}, è il risultato")  # Stampa il risultato della sottrazione

    # Caso per la moltiplicazione
    case "3":
        risultato = n1 * n2  # Moltiplicazione dei due numeri
        print(f"{risultato}, è il risultato")  # Stampa il risultato della moltiplicazione

    # Caso per la divisione
    case "4": 
        if n2 == 0:  # Verifica se il secondo numero è zero
            print("Non è possibile dividere per 0")  # Se il secondo numero è zero, stampa un errore
        else:
            whatdo = input("Preferisci una divisione intera (1), reale (2) o con resto(3)?")
            match whatdo:
                # Divisione intera
                case "1":
                    risultato = n1 // n2  # Divisione del primo numero per il secondo
                    print(f"{risultato}, è il risultato")  # Stampa il risultato della divisione
                # Divisione reale
                case "2":
                    risultato = n1 / n2
                    print(f"{risultato}, è il risultato")
                # Divisione con resto
                case "3":
                    risultato = n1 % n2
                    print(f"{risultato}, e il risultato")
                    
                case _:
                    print("Operazione non valida")
                    

    #Caso per la potenza
    case "5":
        risultato = n1 ** n2
        print(f"{risultato}, è il risultato")
        
    # Caso di default per operazioni non valide
    case _:
        print("Operazione non valida")  # Se l'operazione scelta non è valida, stampa un errore
