def pulizia(stringa): # rripulisce la stringa
    for c in caratteri_da_rimuovere: 
        stringa = stringa.replace(c, "")
    stringa = stringa.split()
    return stringa
    
def contaParole(stringa): # aggiunge ogni parola ad un dizionario, se è già presente ne incrementa il valore
    conteggio = {}
    for parola in stringa:
        if parola in conteggio:
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1

    duplicato = {k : v for k,v in conteggio.items() if v > 1} # stampa solo le parole che sono ripetute più di una volta
    for key, value in duplicato.items(): # lavoro con chiave e valore
        print(f"\nLa parola [{key}] appare [{value}] volte, ed è lunga [{len(key)}]!")

caratteri_da_rimuovere = [",", ".", "!", "?"]
stringa = input("Inserisci la stringa da analizzare: ").lower()

stringa = pulizia(stringa)
contaParole(stringa)