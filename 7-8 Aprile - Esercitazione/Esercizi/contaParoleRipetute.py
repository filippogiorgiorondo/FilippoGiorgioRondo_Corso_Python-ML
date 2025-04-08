def pulizia(stringa): # ripulisce la stringa
    for c in caratteri_da_rimuovere: 
        stringa = stringa.replace(c, "")
    stringa = stringa.split()
    return stringa

def contaParole(stringa): # aggiunge ogni parola a un dizionario, se è già presente ne incrementa il valore
    conteggio = {}
    for parola in stringa:
        if parola in conteggio:
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1

    duplicato = {k : v for k,v in conteggio.items() if v > 1} # seleziona solo le parole ripetute
    if duplicato:  # Se il dizionario non è vuoto
        for key, value in duplicato.items(): 
            print(f"\nLa parola [{key}] appare [{value}] volte, ed è lunga [{len(key)}]!")
    else:
        print("\nNon ci sono parole duplicate.")

caratteri_da_rimuovere = [",", ".", "!", "?"]
stringa = input("Inserisci la stringa da analizzare: ").lower()

stringa = pulizia(stringa) 
contaParole(stringa)
