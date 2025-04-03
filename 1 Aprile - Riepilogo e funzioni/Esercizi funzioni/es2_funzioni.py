lista0 = [0] # Lista per numero massimo 0
lista1 = [0, 1]  # Inizializziamo la lista con i primi due numeri di Fibonacci

n = int(input("Inserisci il numero massimo per la sequenza di Fibonacci: "))

if n == 0: # se l'utente digita 0
    print(f"La sequenza di Fibonacci fino al valore massimo {n} è: {lista0}")
elif n == 1: # se l'utente digita 1
    print(f"La sequenza di Fibonacci fino al valore massimo {n} è: {lista1}")
else:
    # Generiamo la sequenza finché il prossimo numero non supera n
    while True:
        prossimo = lista1[-1] + lista1[-2]  # Sommiamo gli ultimi due numeri della lista
        if prossimo > n:
            break  # Se supera n, interrompiamo il ciclo
        lista1.append(prossimo)  # Aggiungiamo il numero alla lista

    print(f"La sequenza di Fibonacci fino al valore massimo {n} è: {lista1}")
