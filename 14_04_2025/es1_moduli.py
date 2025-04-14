# Esercizio pg.127
class Libro:
    def __init__(self, titolo, autore,isbn):
        self.isbn = 1
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    def descrizione(self):
        print(f"Il libro {self.titolo} è stato scritto da {self.autore}. Il suo ISBN è {self.isbn}")
        
def crea_libro():
    titolo = input("Inserisci il titolo del libro da aggiungere: ")
    autore = input("Inserisci l'autore del tuo libro: ")
    isbn = input("Inserisci l'ISBN del tuo libro: ")
    libro = Libro(titolo, autore, isbn)
    return libro