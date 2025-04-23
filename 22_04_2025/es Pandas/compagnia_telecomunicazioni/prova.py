import pandas as pd
import numpy as np

# === Data Cleaning ===
def clean_data(df):
    df = df.drop_duplicates()
    df['Churn'] = df['Churn'].fillna(df['Churn'].mode()[0])

    # Correzione anomalie
    df = df[(df['Età'] > 0) & (df['Età'] <= 95)]
    df = df[(df['Tariffa_Mensile'] > 0) & (df['Tariffa_Mensile'] < 500)]
    df = df[df['Dati_Consumati'] >= 0]

    # Uniformare formato Churn
    df['Churn'] = df['Churn'].str.upper().str.strip()
    df = df[df['Durata_Abbonamento'] >= 0]
    return df

# === Initial Data Exploration ===
def initial_exploration(df):
    print("General Information:")
    print(df.info())
    print("\nDescriptive Statistics:")
    print(df.describe())
    print("\nChurn Distribution:")
    print(df["Churn"].value_counts())

# === Exploratory Data Analysis (EDA) ===
def exploratory_data_analysis(df):
    df["Costo_per_GB"] = df.apply(
        lambda row: row["Tariffa_Mensile"] / row["Dati_Consumati"]
        if row["Dati_Consumati"] > 0 else np.nan, axis=1
    )

    churn_mean = df.groupby("Churn")[["Età", "Durata_Abbonamento", "Tariffa_Mensile", "Costo_per_GB"]].mean()
    print("\nMean values for Churn Group:")
    print(churn_mean)

    correlation_matrix = df[["Età", "Durata_Abbonamento", "Tariffa_Mensile", "Costo_per_GB"]].corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)

# === Data Preparation for Modeling ===
def prepare_data_for_modeling(df):
    df["Churn"] = df["Churn"].map({"NO": 0, "SÌ": 1})

    numerical_columns = ["Età", "Durata_Abbonamento", "Tariffa_Mensile", "Costo_per_GB"]
    df[numerical_columns] = df[numerical_columns].apply(
        lambda x: (x - x.min()) / (x.max() - x.min())
    )

    print("\nData normalized and prepared for modeling.")
    print(df[numerical_columns + ['Churn']].head())

    return df

# === Main Program ===
def main():
    df = pd.read_csv("C:/Users/filip/Documents/GitHub/FilippoGiorgioRondo_Corso_Python-ML/22_04_2025/es Pandas/compagnia_telecomunicazioni/clienti_dirty.csv")
    df = clean_data(df)

    while True:
        print("\nMenu:")
        print("1. Initial Data Exploration")
        print("2. Exploratory Data Analysis (EDA)")
        print("3. Data Preparation for Modeling")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        match choice:
            case '1':
                initial_exploration(df)
            case '2':
                exploratory_data_analysis(df)
            case '3':
                df = prepare_data_for_modeling(df)
            case '4':
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
