# Funzione per creare una lista di numeri inseriti dall'utente
def creazioneLista():
    print("Benvenuto nella funzione 'quadrato', dovrai inserire una lista di numeri.\n")  # Messaggio di benvenuto
    lista = []  # Creazione di una lista vuota
    quantiNumeri = int(input("Inserisci il numero di valori da aggiungere alla lista: "))  # Richiesta del numero di elementi
    
    for i in range(quantiNumeri):  # Iterazione per il numero di elementi indicato dall'utente
        numero = int(input("\nInserisci il numero da aggiungere alla lista: "))  # Richiesta di un numero
        lista.append(numero)  # Aggiunta del numero alla lista
        print(f"\nLa lista al momento contiene i seguenti valori: {lista}")  # Stampa della lista aggiornata
    
    print("\nOttimo, lista completata") 
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
    return listaQuadrati, sommaQuadrati

# Funzione principale che avvia il programma
def inizio():
    sommaFinale = 0
    while True:
        lista = creazioneLista()  # Chiamata della funzione per creare la lista
        listaQuadrati, sommaQuadrati = quadrato(lista)  
        sommaFinale += sommaQuadrati
        # Chiamata della funzione per calcolare i quadrati e la somma
        print(f"\nLa tua lista dei quadrati è: {listaQuadrati}, e la loro somma è {sommaQuadrati}")  # Stampa del risultato
        whatdo = int(input("Vuoi aggiungere un'altra lista, premere 1 per continuare: "))
        if whatdo == 1:
            print(f"\n\nAl momento la somma totale dei quadrati di tutti i tuoi numeri è: {sommaFinale} ..continuiamo\n")
        else:
            break
# Avvia il programma
inizio()
