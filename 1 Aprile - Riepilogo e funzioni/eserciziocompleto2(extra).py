import random

listaPari = []
listaDispari = []
totalePari = 0
totaleDispari = 0
numInserito = 0 # Creo la variabile per il ciclo while
primo = True

while numInserito <= 0: # Continua a richiedere in input un numero positivo
    numInserito = int(input("Inserisci un numero che sia maggiore di 0: "))
    print("Ottimo, hai inserito un numero positivo")

limiteInferiore = int(input("Inserisci il numero minimo RANDOM per la lista"))
limiteSuperiore = int(input("Inserisci il numero max RANDOM per la lista"))

listaCasuale = [random.randint(limiteInferiore, limiteSuperiore) for _ in range(numInserito)]

for _ in listaCasuale: # Prende ogni valore dalla lista e verifica che sia pari o dispari per aggiungerlo alla lista corretta
    if _ % 2 == 0:
        listaPari.append(_)
        totalePari = totalePari + _
    else:
        listaDispari.append(_)
        totaleDispari = totaleDispari + _
        
    # Verifica che il numero interessato sia primo   
    if numInserito <2:
        print(f"{_}, non è un numero primo")
    
    elif any(numInserito % i == 0 for i in range(2, int(numInserito ** 0.5) + 1)):
        primo = False
    
    else:
        primo = True
    
    print(f"Per ogni elemento della lista, vedremo se è primo o meno\nIl numero {_}  è primo? .....suspance....: {primo}") 
    
print(f" La somma dei numeri pari è: {totalePari}, mentre la somma dei numeri dispari è: {totaleDispari}")
        
# Funzione per stampare uno ad uno, ogni elemento della liste considerate  
print("Di seguito tutti i numeri pari della lista:")    
for _ in listaPari:
    print(_)

print("Di seguito tutti i numeri dispari della lista")
for _ in listaDispari:
    print(_)