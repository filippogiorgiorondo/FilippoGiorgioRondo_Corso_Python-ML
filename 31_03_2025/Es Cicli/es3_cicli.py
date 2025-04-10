listaPrimi = []

while len(listaPrimi) <= 5:  # Il ciclo si interrompe quando ha trovato 5 numeri primi
    numeroInserito = int(input("Inserisci un numero per verificare che sia primo: "))

    if numeroInserito < 2:  # I numeri minori di 2 non sono primi
        print(f"{numeroInserito} NON è un numero primo")
        continue  # Torna all'inizio del ciclo

    primo = True  # Suppendo che il numero sia primo...

    # Se il numeroInserito è divisibile per un numero più grande della sua radice quadrata, allora avrà già un divisore più piccolo trovato prima
    for i in range(2, int(numeroInserito ** 0.5) + 1): 
        
        if numeroInserito % i == 0:  # Se è divisibile, allora NON è primo
            print(f"{numeroInserito} NON è un numero primo")
            primo = False
            break  # Uscire dal ciclo, non serve controllare oltre

    if primo:  # Se dopo il ciclo è ancora "True", il numero è primo
        print(f"{numeroInserito} è un numero primo")
        listaPrimi.append(numeroInserito)  # Il numero viene aggiunto alla lista

print(f"I 5 numeri primi inseriti sono: {listaPrimi}")
