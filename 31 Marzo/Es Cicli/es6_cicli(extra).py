whatdo = input("Pari o dispari (1)\nUtilizzo while(2)\nUtilizzo range(3)\nUtilizzo for(4)\nEsercizio misto(5): ")
match whatdo:
    case "1":
        # Programma pari o dispari
        numero = int(input("Inserisci un numero: "))

        if numero % 2 == 0: #un numero è pari se il resto della sua divisione per 2 è nullo
            print("Il tuo numero è pari")
        else:
            print("Il tuo numero è dispari") #altrimenti il numero è dispari
    case "2":
        # Utilizzo di while
        numero = int(input("Inserisci qui un numero maggiore di 0: "))
        while numero >= 0:
            print(numero)
            numero = numero - 1
    case "3":
        # Utilizzo di range
        numero = int(input("Inserisci qui un numero maggiore di 0: "))
        for n in range(numero, -1, -1):
            print(n)
    case "4":
        # Utilizzo di for
        lista = [1,2,4,5,6,245,5]
        n = 0
        for n in lista:
            print(n ** 2)
    case "5":
        # Lista valorizzata dall'utente
        lista2 = []

        # Inserimento valori nella lista
        for n in range(1, 6):
            print(f"Inserisci il {n} numero da aggiungere alla lista")
            numeroAggiunto = int(input())
            lista2.append(numeroAggiunto)
            print("Numero aggiunto con successo")

        # Ricerca del valore massimo
        max = 0  # inizializziamo a con un valore di partenza
        for n in lista2:  # n è il valore dell'elemento, non l'indice
            if n >= max:   # confrontiamo il valore n con a
                max = n    # se n è maggiore o uguale ad a, a diventa n
        else:
            pass

        print(f"Il valore massimo nella lista è: {max}")

        # Ciclo while per contare i numeri della lista
        n = 1
        while n <= len(lista2):
            n += 1
            print(f"{len(lista2)} è la lunghezza massima")
