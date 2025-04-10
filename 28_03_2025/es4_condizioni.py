credenziali = ["Admin", "12345"]

# Richiede all'utente di inserire nome utente e password
nome = input("Inserisci il nome utente (occhio alle maiuscole e minuscole): ")
# Converte l'input in stringa (ridondante, ma mantenuto)
password = str(input("Inserisci la password utente (occhio alle maiuscole e minuscole): "))

# Verifica che le credenziali siano corrette
if nome == credenziali[0] and password == credenziali[1]:
    print("Benvenuto!")

# Se le credenziali non sono corrette, richiede all'utente come procedere
else:
    num = str(("Credenziali errate. Premere 1 per ritentare o premere 2 per recuperare la password: "))
    
    # L'utente sceglie se ritentare il login o recuperare la password
    match num: #struttura di controllo
        case "1":
            # Nuovo tentativo di login
            nome = input("Inserisci il nome utente (occhio alle maiuscole e minuscole): ")
            password = str(input("Inserisci la password utente (occhio alle maiuscole e minuscole): "))
            # Se le credenziali sono corrette, viene confermato l'accesso; altrimenti il programma si arresta
            if nome == credenziali[0] and password == credenziali[1]:
                print("Benvenuto")
            else:
                print("Tentativo di login fallito, arresto del programma")
    
        case "2":
            # Procedura di recupero password tramite domanda di sicurezza
            numPref = 13
            numScelto = int(input("Inserisci il tuo numero preferito: "))
            # Se la risposta è corretta, l'utente può impostare una nuova password
            if numScelto == numPref:
                nuovaPassword = input("Complimenti, accesso confermato. Inserisci la tua nuova password: ")
                credenziali[1] = nuovaPassword  # Sostituisce la vecchia password con la nuova
                print("Password modificata con successo")
            else:
                print("Risposta errata. Tentativo di login fallito, arresto del programma")
    
        case _: #caso default, viene eseguito se le condizioni precedenti non sono soddisfatte
            print("Opzione non valida")