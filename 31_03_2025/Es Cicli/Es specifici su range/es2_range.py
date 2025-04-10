while True:
    estremoInferiore = int(input("Inserisci l'estremo inferiore del range: "))
    estremoSuperiore = int(input("Inserisci l'estremo superiore del range: "))
    listaPrimo = []
    listaNonPrimo = []
    
    if estremoInferiore > estremoSuperiore:
        # Scambio gli estremi per gestire il caso in cui il primo sia maggiore del secondo
        estremoInferiore, estremoSuperiore = estremoSuperiore, estremoInferiore
    
    # Gestione dell'intervallo in ordine crescente
    for i in range(estremoInferiore, estremoSuperiore + 1):  # +1 per includere l'estremo superiore
        if i < 2:
            listaNonPrimo.append(i)  # 0 e 1 non sono primi
        else:
            primo = True
            for j in range(2, int(i ** 0.5) + 1):  # Verifica divisibilità fino alla radice quadrata
                if i % j == 0:  # Se è divisibile, allora NON è primo
                    listaNonPrimo.append(i)
                    primo = False
                    break
            
            # Aggiungi alla lista dei primi solo se è primo
            if primo:
                listaPrimo.append(i)
    
    print(f"La lista dei numeri primi compresi nel tuo range è {listaPrimo}")
    print(f"La lista dei numeri non primi compresi nel tuo range è {listaNonPrimo}")

    whatdo = int(input("Premere 1 per interrompere, premere un numero qualsiasi per ricominciare"))
    if whatdo == 1:
        break
