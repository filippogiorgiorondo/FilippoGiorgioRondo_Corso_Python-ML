listaPari = []

while len(listaPari) <= 5: # Ciclo che si ripete finchè la lista non è composta da 5 valori
    
    numeroInserito = int(input("Inserisci un numero per verificare che sia pari o dispari: "))
 
    if numeroInserito % 2 == 0: # Un numero è pari se il resto della sua divisione per 2 è nullo
        print("Il tuo numero è pari")
        listaPari.append(numeroInserito) # Aggiunge alla lista il numero pari
    else:
        print("Il tuo numero è dispari") # Altrimenti il numero è dispari
    