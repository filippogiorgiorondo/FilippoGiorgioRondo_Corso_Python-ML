# Lista valorizzata dall'utente
lista = []

 # Inserimento valori nella lista
for n in range(1, 6):
    print(f"Inserisci il {n} numero da aggiungere alla lista")
    numeroAggiunto = int(input())
    lista.append(numeroAggiunto)
    print("Numero aggiunto con successo")

# Ricerca del valore massimo
max = 0  # inizializziamo a con un valore di partenza
for n in lista:  # n è il valore dell'elemento, non l'indice
    if n >= max:   # confrontiamo il valore n con a
        max = n    # se n è maggiore o uguale ad a, a diventa n
    else:
        pass

print(f"Il valore massimo nella lista è: {max}")

#Ciclo while per contare i numeri della lista
n = 1
while n <= len(lista):
    n += 1
print(f"{n} è il numero massimo, {len(lista)} è la lunghezza massima")
