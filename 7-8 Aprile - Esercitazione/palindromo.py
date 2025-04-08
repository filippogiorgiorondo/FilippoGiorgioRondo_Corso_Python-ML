def palindromo(stringa):
    if stringa == stringa[::-1]: #riprende la stringa in input e la legge al contrario per confrontarla
        print("è un palindromo")
    else:
        print("non è un palindromo")
    
stringa = input("Inserisci la tua parola o frase: ").lower() # trasforma in minuscolo tutti i caratteri

caratteri_da_rimuovere = [" ", ",", ".", "!", "?"]
stringa = ".!?"

for c in caratteri_da_rimuovere: # per ogni elemento della lista, rimuove il carattere interessato
    stringa = stringa.replace(c, "")

palindromo(stringa) # passa alla funzione l'input validato