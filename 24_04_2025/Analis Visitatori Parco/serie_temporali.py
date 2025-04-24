import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Alternativa elegante e integrata


# === Generazione dei dati ===
def generate_data():
    dates = pd.date_range(start="2023-01-01", periods=365, freq='D')
    np.random.seed(42)
    visitors = np.random.normal(loc=2000, scale=500, size=365) + np.linspace(0, 1000, 365)
    df = pd.DataFrame({'Visitors': visitors}, index=dates)
    return df

# === Analisi dei dati ===
def analyze_data(df):
    monthly_stats = df.resample('ME').agg({'Visitors': ['mean', 'std']})
    print("\nMedia e Deviazione Standard Mensile dei Visitatori:")
    print(monthly_stats)

def plot_daily_visitors(df):
    df['7_day_avg'] = df['Visitors'].rolling(window=7).mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Visitors'], label='Daily Visitors', color='#4A90E2', linewidth=1.5, alpha=0.7)
    plt.plot(df.index, df['7_day_avg'], label='7-Day Moving Average', color='#D0021B', linewidth=2.5)
    
    plt.title('Daily Visitors with 7-Day Moving Average', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Visitors', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_monthly_averages(df):
    monthly_avg = df.resample('ME').mean()
    
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_avg.index, monthly_avg['Visitors'], marker='o', color='#7ED321', linewidth=2, label='Monthly Average')
    
    plt.title('Monthly Average Visitors', fontsize=16, fontweight='bold')
    plt.xlabel('Month', fontsize=12, fontweight='bold')
    plt.ylabel('Average Visitors', fontsize=12, fontweight='bold')
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# === Menu interattivo con match-case ===
def main_menu():
    df = generate_data()
    while True:
        print("\n--- MENU ---")
        print("1. Analisi mensile (media e deviazione standard)")
        print("2. Grafico giornaliero con media mobile a 7 giorni")
        print("3. Grafico media mensile")
        print("4. Esci")

        choice = input("Scegli un'opzione (1/2/3/4): ")
        match choice:
            case '1':
                analyze_data(df)
            case '2':
                plot_daily_visitors(df)
            case '3':
                plot_monthly_averages(df)
            case '4':
                print("Uscita in corso...")
                break
            case _:
                print("Scelta non valida. Riprova.")

# === Avvio del programma ===
if __name__ == "__main__":
    main_menu()
