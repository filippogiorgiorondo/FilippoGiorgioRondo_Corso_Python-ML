import pandas as pd
import numpy as np

# Imposta il seed per la riproducibilità
np.random.seed(42)

# Parametri
date_range = pd.date_range(start="2025-04-01", end="2025-04-30")
città = ["Milano", "Roma", "Napoli"]
prodotti = ["Laptop", "Smartphone", "Tablet"]

# Generazione del dataset
n_rows = 200
dati = {
    "Data": np.random.choice(date_range, size=n_rows),
    "Città": np.random.choice(città, size=n_rows),
    "Prodotto": np.random.choice(prodotti, size=n_rows),
    "Vendite": np.random.randint(100, 2000, size=n_rows)
}

df = pd.DataFrame(dati)

# Tabella Pivot: vendite medie per prodotto e città
pivot_table = df.pivot_table(
    values="Vendite",
    index="Prodotto",
    columns="Città",
    aggfunc="mean"
)

# GroupBy: vendite totali per prodotto
vendite_totali = df.groupby("Prodotto")["Vendite"].sum().reset_index()

# Output
print("==== Dataset Iniziale ====")
print(df.head(), "\n")

print("==== Tabella Pivot (Vendite Medie per Prodotto e Città) ====")
print(pivot_table, "\n")

print("==== Vendite Totali per Prodotto ====")
print(vendite_totali)

# Salva la tabella pivot in un file CSV
pivot_table.to_csv("pivot_vendite.csv", sep=";", encoding="utf-8")

print("✅ Tabella pivot salvata con successo in 'pivot_vendite.csv'")

