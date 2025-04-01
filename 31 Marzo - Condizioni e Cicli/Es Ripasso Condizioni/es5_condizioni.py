# Input trasformato in numero intero per verificare l'età
eta = int(input("Benvenuto! Prima di veder il film, ti chiediamo di inserire la tua età: "))

# Blocco condizione per verificare che sia maggiorenne
if eta >= 18:
    print("Perfetto, puoi vedere il film")

# Se la condizione precedente non è verificata, viene impedita la visione del film
else:
    print("I minorenni non possono vedere il film")
