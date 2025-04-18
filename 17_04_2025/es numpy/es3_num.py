import numpy as np

# Genera matrice 6x6 dei numeri compresi tra 1 e 100
matrice = np.random.randint(101, size = (6,6))
print("Matrice originale:\n", matrice)

# Genera la sottomatrice centrale 4x4
matrice_centrale = matrice[1:5, 1:5]
print("\nSotto-matrice centrale 4x4:\n", matrice_centrale)

# Inverte le righe della sottomatrice
matrice_invertita = matrice_centrale[::-1, ::]
print("\nSottomatrice invertita:\n", matrice_invertita)

# Calcola la diagonale della sottomatrice. 
# item() per restituire il valore puro perchè i valori vengono estratti come array
diagonale = [matrice_centrale[i,i].item() for i in range(matrice_centrale.shape[0])]
print("\nDiagonale sottomatrice:\n", diagonale)

# Sostituisce tutti i multipli di 3 con il loro valore diminuito di 1 nella matrice invertita
for j in range(matrice_invertita.shape[0]): # Prende il numero delle righe
    for k in range(matrice_invertita.shape[1]): # Prende il numero delle colonne
        if matrice_invertita[j,k] % 3 == 0:
            matrice_invertita[j,k] = -1
print("\nMatrice invertita modificata:\n", matrice_invertita)