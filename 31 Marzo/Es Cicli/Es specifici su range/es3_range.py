while True: 
    # Chiediamo due numeri all'utente
    num1 = int(input("Inserisci il primo numero: "))
    num2 = int(input("Inserisci il secondo numero: "))

    # Lista per i fattori comuni
    fattori_comuni = []

    # Troviamo i fattori comuni
    for i in range(1, min(num1, num2) + 1):  # Iteriamo fino al più piccolo dei due numeri
        if num1 % i == 0 and num2 % i == 0:
            fattori_comuni.append(i)

    # Stampiamo il risultato
    if fattori_comuni == [1]:  # Se l'unico fattore comune è 1
        print("I numeri sono coprimi.")
    else:
        print("Fattori comuni:", fattori_comuni)

    # Chiediamo due stringhe all'utente
    str1 = input("Inserisci la prima stringa: ")
    str2 = input("Inserisci la seconda stringa: ")

    # Controlliamo se hanno le stesse lettere (cioè sono complementari secondo la traccia)
    set1 = set1.sort()
    set2 = set2.sort()

    if set1 == set2:  # Confrontiamo i due insiemi di caratteri
        print("Le stringhe sono complementari.")
    else:
        print("Le stringhe NON sono complementari.")

    # Chiediamo se l'utente vuole ripetere
    ripeti = input("Vuoi ripetere il programma? (s/n): ").lower()
    if ripeti != "s":
        break  # Esce dal ciclo while se l'utente non vuole ripetere
