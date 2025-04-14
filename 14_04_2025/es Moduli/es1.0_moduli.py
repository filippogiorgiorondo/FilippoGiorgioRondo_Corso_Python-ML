import es1_moduli as em

class Libreria:
    def __init__(self): # metodo costruttore
        self.catalogo = {}
        self.id = 1
    def aggiungi_libro(self): # funzione per aggiungere un libro al dizionario
        libro = em.crea_libro()
        self.catalogo[self.id] = libro
        self.id += 1

    def rimuovi_libro(self): # funzione per rimuovere un libro in base a ISBN
        isbn_rimuovere = input("Inserisci l'ISBN del libro da rimuovere: ")
        for chiave, libro in list(self.catalogo.items()): 
            if libro.isbn == isbn_rimuovere:
                del self.catalogo[chiave]
                print(f"Libro con ISBN {isbn_rimuovere} rimosso.")
                return
        print("Nessun libro trovato con l'ISBN inserito.")
    def mostra_catalogo(self): # stampa tutti gli id presenti nel dizionario e utilizza il metodo descrizione per ogni libro
        if self.catalogo == {}:
            print("Catalogo vuoto")
        for chiave, libro in self.catalogo.items():
            print(f"ID {chiave}")
            libro.descrizione()

def menu():
    libreria = Libreria()

    while True:
        print("\n📚 MENU LIBRERIA 📚")
        print("1. Mostra catalogo")
        print("2. Aggiungi libro")
        print("3. Rimuovi libro")
        print("4. Esci")

        scelta = input("Seleziona un'opzione (1-4): ")

        match scelta:
            case "1":
                libreria.mostra_catalogo()
            case "2":
                libreria.aggiungi_libro()
            case "3":
                libreria.rimuovi_libro()
            case "4":
                print("Uscita dal programma.")
                break
            case _:
                print("Scelta non valida. Riprova.")
                
menu()
