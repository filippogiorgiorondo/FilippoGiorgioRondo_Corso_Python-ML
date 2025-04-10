#creare lista che contiene gli account
accounts = []

#lista annidata che si inserisce all'interno della lista accounts
accountesempio = ["accountesempio","111"]
accounts.append(accountesempio)

#id per riuscire ad individuare la lista interessata all'interno della lista accounts (posizione lista all'interno di accounts)
id_account_esempio = 0
id_account = 0

#richiedere l'azione desiderata
whatdo = input("Vuoi creare un nuovo account o accedere all'account esistente (1 o 2): ")

#creazione account con trasformazione del nome in minuscolo
if whatdo == "1":
    accountname = input("Inserisci il nome del tuo account: ").lower() 
    name = accountname
    
    #verifica che il nome account inserito esista già 
    if accounts[id_account_esempio][0] == accountname:
        print("Nome già in uso")
    else:
        #se il nome non esiste crea una lista con i parametri inseriti
        accountname = []
        #aggiunge alla accounts la lista appena creata
        accountname.append(name)
        id_account += 1 #aumenta di un valore così da poter indicare la posizione corretta della lista all'interno di accounts
        #richiede in input la password e la memorizza nella lista
        accountpassword = input("Inserisci la tua password: ")
        accountname.append(accountpassword)
        print(f"Ottimo, il tuo account è stato aggiunto con successo\nNome account: {accountname[0]}, Id account: {id_account}, Password: {accountname[1]}")

#condizione per effettuare il login, verifa che i dati inseriti coincidano con quelli presenti nella lista di riferimento
elif whatdo == "2":
    loginid = int(input("Inserisci l'id del tuo account: ")) #numero utilizzato per trovare la lista interesssata dentro accounts
    loginname = input("Inserisci il nome del tuo account: ").lower()
    loginpassword = input("Inserisci la password del tuo account: ")
    
    #verifica che le credenziali coincidano
    if loginname == accounts[loginid][0] and loginpassword == accounts[loginid][1]:
        print("Accesso effettuato")
    else:
        print("Credenziali errate")

#condizione per input non valido
else:
    print("Numero inserito non valido")