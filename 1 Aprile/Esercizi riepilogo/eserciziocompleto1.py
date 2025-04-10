numInserito = 0 #creo la variabile per il ciclo while
listaPari = [] 
listaDispari = []
primo = True

while numInserito <= 0: #continua a richiedere in input un numero positivo
    numInserito = int(input("Inserisci un numero che sia maggiore di 0: "))
    print("Ottimo, hai inserito un numero positivo")

numeroLimite = numInserito + 1 #per considerare il numero limite poichè range lo esclude

for n in range(1, numeroLimite):
    if n % 2 == 0: #verifica che sia pari e lo aggiunge alla lista
        listaPari.append(n)
    else: #se la condizione precedente non è verificata, il numero viene aggiunto alla lista dispari
        listaDispari.append(n)
        
print(f"I numeri pari sono: {listaPari}, mentre i numeri dispari sono: {listaDispari}")

if numInserito <2:
    print("Il numero inserito non è un numero primo")
    
elif any(numInserito % i == 0 for i in range(2, int(numInserito ** 0.5) + 1)):
    primo = False
    
print(f"Il numero inserito è primo? .....suspance....: {primo}") 