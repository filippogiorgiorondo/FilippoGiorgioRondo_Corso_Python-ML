# Programma pari o dispari
numero = int(input("Inserisci un numero: "))

if numero % 2 == 0: #un numero è pari se il resto della sua divisione per 2 è nullo
    print("Il tuo numero è pari")
else:
    print("Il tuo numero è dispari") #altrimenti il numero è dispari
    
# Utilizzo di while
numero = int(input("Inserisci qui un numero maggiore di 0: "))
while numero >= 0:
    print(numero)
    numero = numero - 1
    
# Utilizzo di range
numero = int(input("Inserisci qui un numero maggiore di 0: "))
for n in range(numero, -1, -1):
    print(n)
    
# Utilizzo di for
lista = [1,2,4,5,6,245,5]
n = 0
for n in lista:
    print(n **2)
