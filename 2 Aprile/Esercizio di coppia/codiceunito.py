import random

# Lista dei concerti disponibili
listaConcerti = [
    "Tiziano Ferro", 
    "Shade", 
    "Mirko Camparus", 
    "Geolier", 
    "Malgioglio", 
    "Gigi D'Alessio"
]

# Dizionario che tiene traccia dei posti disponibili per ogni concerto (massimo 10 posti per concerto)
postiDisponibili = {concerto: 10 for concerto in listaConcerti}

# Dizionario che memorizza gli utenti registrati (chiave: nome utente, valore: password)
utentiRegistrati = {}

def sign_in():
    """Registra un nuovo utente con nome e password"""
    name = input("Inserisci il tuo nome: ")
    
    # Controlla se l'utente esiste già
    if name in utentiRegistrati:
        print("Questo nome utente è già registrato. Scegli un altro nome.")
        return None
    
    # Richiede una password con almeno un carattere speciale (@, #, +)
    password = input("Inserisci una password (deve contenere almeno un simbolo @, # o +): ")
    
    # Controlla se la password contiene almeno uno dei simboli richiesti
    if any(s in password for s in ["@", "#", "+"]):
        utentiRegistrati[name] = password  # Salva l'utente nel dizionario
        print("Registrazione completata con successo!")
        return name
    else:
        print("La password non è abbastanza sicura. Usa almeno uno dei simboli @, # o +.")
        return None

def login():
    """Permette a un utente di accedere"""
    name = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password: ")
    
    # Controlla se il nome utente esiste e la password corrisponde
    if utentiRegistrati.get(name) == password:
        print("Accesso effettuato con successo!")
        return name
    else:
        print("Nome utente o password errati.")
        return None

def ha_password_segreta():
    """Controlla se l'utente conosce la password segreta per aggiungere concerti"""
    password_segreta = input("Inserisci la password segreta: ")
    return password_segreta == "GHIBLI"  # La password segreta per aggiungere concerti è "GHIBLI"

def aggiuntaPosti(concerto):
    """Aggiunge un partecipante a un concerto se ci sono posti disponibili"""
    if postiDisponibili[concerto] > 0:
        postiDisponibili[concerto] -= 1  # Riduce il numero di posti disponibili
        print(f"Prenotazione confermata per {concerto}! Posti rimanenti: {postiDisponibili[concerto]}")
        return True
    else:
        print("Posti esauriti per questo concerto.")
        return False

def prenotaConcerto():
    """Permette a un utente di prenotare fino a 3 concerti"""
    concertiPrenotati = []  # Lista dei concerti prenotati dall'utente

    # Mostra i concerti disponibili con il numero di posti rimasti
    print("Concerti disponibili:")
    for i, concerto in enumerate(listaConcerti):
        print(f"{i} - {concerto} ({postiDisponibili[concerto]} posti disponibili)")

    # L'utente può prenotare fino a 3 concerti
    for _ in range(3):
        scelta = input("Inserisci il numero del concerto che vuoi prenotare (o premi Invio per terminare): ")
        
        if scelta == "":  # Se l'utente preme Invio, termina la selezione
            break

        if scelta.isdigit():
            scelta = int(scelta)
            if 0 <= scelta < len(listaConcerti):  # Verifica se la scelta è valida
                concerto_scelto = listaConcerti[scelta]
                if aggiuntaPosti(concerto_scelto):  # Controlla la disponibilità
                    concertiPrenotati.append(concerto_scelto)
            else:
                print("Scelta non valida.")
        else:
            print("Inserisci un numero valido.")

    print("I tuoi concerti prenotati:", concertiPrenotati)

def aggiungiConcerto():
    """Permette di aggiungere un concerto se si conosce la password segreta"""
    if ha_password_segreta():  # Controlla se l'utente ha la password segreta "GHIBLI"
        nuovo_concerto = input("Inserisci il nome del nuovo concerto: ")
        if nuovo_concerto not in listaConcerti:
            listaConcerti.append(nuovo_concerto)  # Aggiunge il concerto alla lista
            postiDisponibili[nuovo_concerto] = 10  # Imposta il numero di posti disponibili a 10
            print(f"Concerto '{nuovo_concerto}' aggiunto con successo!")
        else:
            print("Questo concerto esiste già.")
    else:
        print("Password segreta errata. Non puoi aggiungere concerti.")

def main():
    """Gestisce il flusso principale del programma"""
    print("Benvenuto nel sistema di prenotazione concerti!")
    
    while True:
        # L'utente può scegliere se registrarsi, accedere o uscire
        scelta = input("Vuoi registrarti (R), accedere (L) o uscire (E)? ").upper()

        if scelta == "R":
            utente = sign_in()  # Registra un nuovo utente
        elif scelta == "L":
            utente = login()  # Effettua il login
            if utente:
                while True:
                    # Dopo il login, l'utente può prenotare, aggiungere concerti o disconnettersi
                    azione = input("Vuoi prenotare un concerto (P), aggiungere un concerto (A) o fare logout (L)? ").upper()
                    match azione:
                        case "P":
                            prenotaConcerto()  # L'utente prenota un concerto
                        case "A":
                            aggiungiConcerto()  # L'utente aggiunge un nuovo concerto (se ha la password segreta)
                        case "L":
                            break
                        case _:
                            print("Scelta non valida")
        elif scelta == "E":
            print("Grazie per aver usato il sistema di prenotazione!")
            break  # Termina il programma
        else:
            print("Scelta non valida.")

# Avvia il programma
main()
