position_to_letter = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 
    10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 
    18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 
    26: 'Z'
}

# Invertiamo il dizionario per una ricerca più rapida
letter_to_position = {v: k for k, v in position_to_letter.items()}

caratteri_da_rimuovere = [",", ".", "!", "?"] 

def pulizia(stringa):  # Ripulisce la stringa da caratteri speciali
    for c in caratteri_da_rimuovere: 
        stringa = stringa.replace(c, "")
    return stringa

def cripta(stringa):
    nuovoTesto = ""
    for lettera in stringa:
        if lettera in letter_to_position:
            posizione = letter_to_position[lettera]
            nuova_posizione = (posizione + chiave) % 26  # Shift di 2 con ciclo
            if nuova_posizione == 0:  # Se la posizione arriva a 0, significa che è la lettera 'Z'
                nuova_posizione = 26
            nuovoTesto += position_to_letter[nuova_posizione]
        else:
            nuovoTesto += lettera  # Mantiene i caratteri non alfabetici invariati
    return nuovoTesto

def decripta(stringa):
    nuovoTesto = ""
    for lettera in stringa:
        if lettera in letter_to_position:
            posizione = letter_to_position[lettera]
            nuova_posizione = (posizione - chiave) % 26  # Shift di -2 con ciclo
            if nuova_posizione == 0:  # Se la posizione arriva a 0, significa che è la lettera 'Z'
                nuova_posizione = 26
            nuovoTesto += position_to_letter[nuova_posizione]
        else:
            nuovoTesto += lettera  # Mantiene i caratteri non alfabetici invariati
    return nuovoTesto

while True: # menu a scelta per criptare, decriptare o uscire
    scelta = int(input("Digita 1 per criptare una stringa. Inserisci 2 per decriptare la stringa. Inserisci 3 per uscire: "))
    match scelta:      
        case 1:
            stringa = input("Inserisci il testo da cifrare: ").upper()
            chiave = int(input("Inserisci un intero per cifrare: "))
            stringa = pulizia(stringa)
            nuovoTesto = cripta(stringa)
            print(f"Testo cifrato: {nuovoTesto}")
            
        case 2:
            stringa = input("Inserisci il testo da decifrare: ").upper()
            chiave = int(input("Inserisci un intero per decifrare: "))
            stringa = pulizia(stringa)
            nuovoTesto = decripta(stringa)
            print(f"Testo decifrato: {nuovoTesto}")
        
        case 3:
            print("Uscita dal programma.")
            break

        case _:
            print("Scelta non valida.")



