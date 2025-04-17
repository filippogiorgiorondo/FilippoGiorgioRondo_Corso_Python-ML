import random
import numpy as np

# Crea un array di 20 numeri interi casuali tra 10 e 50 (inclusi 10, escluso 51)
arr = np.random.randint(10, 51, size=20)
print(arr)

#Slicing dei primi 10 elementi
primi_10 = arr[:10]
print(primi_10)

# Slicing per stampare gli ultimi 5 numeri
ultimi_5 = arr[-1:-6:-1]
print(ultimi_5)

