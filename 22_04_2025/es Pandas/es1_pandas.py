import pandas as pd
import numpy as np

# Imposta il numero di righe
n = 100

# Genera i dati casuali
data = {
    'Nome': ['Nome' + str(i) for i in range(1, n+1)],
    'Età': np.random.randint(18, 80, size=n),
    'Città': np.random.choice(['Roma', 'Milano', 'Torino', 'Napoli'], size=n),
    'Salario': np.random.randint(15000, 80000, size=n)
}

# Crea il DataFrame
df = pd.DataFrame(data)

# Visualizza le prime 5 righe
print(df.head(11))

# Visualizza le ultime 5 righe
print(df.tail())

# Visualizza il tipo di dato per ogni colonna
print(df.dtypes)

print(df['Età'])