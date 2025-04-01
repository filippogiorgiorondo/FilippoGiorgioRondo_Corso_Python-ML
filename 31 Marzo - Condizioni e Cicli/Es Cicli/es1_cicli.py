print("Benvenuto del programma countdown!")
#richiede un numero che viene trasformato in intero
numero = int(input("Inserisci un numero per iniziare il conto alla rovescia: "))

#ciclo che inizia dal numero inserito e si ripete fino a -1 (non incluso, si stoppa a 0), con lo step di -1 quindi il valore da ogni reiterazione diminuisce il valore di 1
for i in range(numero, -1, -1):
    print(i)