def creazioneLista():
    print("Benvenuto nella funzione 'quadrato', dovrai inserire una lista di numeri.")  # Messaggio di benvenuto
    lista = []
    quantiNumeri = int(input("Inserisci il numero di valori da aggiungere alla lista: "))  # Richiesta del numero di elementi
    
    for i in range(quantiNumeri):  # Iterazione per il numero di elementi indicato dall'utente
        numero = int(input("Inserisci il numero da aggiungere alla lista: "))
        lista.append(numero)  # Aggiunta del numero alla lista
        print(f"La lista al momento contiene i seguenti valori: {lista}")  # Stampa della lista aggiornata
    
    print("Ottimo, lista completata")
    return lista  # Restituisce la lista all'utente

# Funzione che calcola il quadrato di ogni elemento nella lista e somma i quadrati
def quadrato(lista):
    listaQuadrati = [] 
    sommaQuadrati = 0 
    
    for i in lista:  # Iterazione sugli elementi della lista
        quadrato = i ** 2 
        sommaQuadrati += quadrato  # Aggiunta del quadrato alla somma totale
        listaQuadrati.append(quadrato)  # Aggiunta del quadrato alla lista
    
    # Restituisce la lista dei quadrati e la somma totale in una stringa
    return f"La lista dei quadrati è {listaQuadrati}, la somma di tali numeri è: {sommaQuadrati}"

# Funzione principale che avvia il programma
def inizio():
    lista = creazioneLista()  # Chiamata della funzione e memorizza in variabile
    risultato = quadrato(lista)  # Chiamata della funzione e memorizza in variabile
    print(risultato)  # Stampa del risultato

# Avvia il programma
inizio()
