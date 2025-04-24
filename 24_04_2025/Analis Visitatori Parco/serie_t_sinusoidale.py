import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Elegant and integrated alternative for plot styling


# === Data Generation with Seasonality ===
def generate_data():
    # Generate dates for the year (365 days)
    dates = pd.date_range(start="2023-01-01", periods=365, freq='D')
    
    np.random.seed(42)  # Set seed for reproducibility

    # Linear increasing trend to simulate growing popularity
    trend = np.linspace(0, 1000, 365)

    # Seasonal component (1 cycle per year -> 2π over 365 days)
    seasonal = 300 * np.sin(2 * np.pi * np.arange(365) / 365)

    # Random noise with mean 2000 and standard deviation 500 to simulate variability in daily visits
    noise = np.random.normal(loc=2000, scale=500, size=365)

    # Combine the noise, trend, and seasonal effect to generate the visitors data
    visitors = noise + trend + seasonal
    
    # Create a DataFrame with dates as the index and visitors as the column
    df = pd.DataFrame({'Visitors': visitors}, index=dates)
    return df


# === Data Analysis ===
def analyze_data(df):
    # Resample the data by month and calculate mean and standard deviation
    monthly_stats = df.resample('ME').agg({'Visitors': ['mean', 'std']})
    
    # Output the monthly statistics (mean and standard deviation)
    print("\nMonthly Mean and Standard Deviation of Visitors:")
    print(monthly_stats)

# === Plotting Daily Visitors with 7-Day Moving Average ===
def plot_daily_visitors(df):
    # Calculate 7-day moving average
    df['7_day_avg'] = df['Visitors'].rolling(window=7).mean()
    
    # Create a plot for daily visitors and the 7-day moving average
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Visitors'], label='Daily Visitors', color='#4A90E2', linewidth=1.5, alpha=0.7)
    plt.plot(df.index, df['7_day_avg'], label='7-Day Moving Average', color='#D0021B', linewidth=2.5)
    
    # Customize the plot aesthetics
    plt.title('Daily Visitors with 7-Day Moving Average', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Visitors', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

# === Plotting Monthly Averages ===
def plot_monthly_averages(df):
    # Resample the data by month and calculate the monthly mean
    monthly_avg = df.resample('ME').mean()
    
    # Create a plot for the monthly average visitors
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_avg.index, monthly_avg['Visitors'], marker='o', color='#7ED321', linewidth=2, label='Monthly Average')
    
    # Customize the plot aesthetics
    plt.title('Monthly Average Visitors', fontsize=16, fontweight='bold')
    plt.xlabel('Month', fontsize=12, fontweight='bold')
    plt.ylabel('Average Visitors', fontsize=12, fontweight='bold')
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


# === Export DataFrame to CSV or JSON ===
def export_data(df):
    print("\n--- Export Data ---")
    print("1. Export as CSV")
    print("2. Export as JSON")
    print("3. Cancel")

    # Get the user's choice for the export format
    choice = input("Choose an option (1/2/3): ")
    
    match choice:
        case '1':
            file_name = input("Enter file name for CSV (e.g., visitors_data.csv): ")
            df.to_csv(file_name)
            print(f"Data successfully exported as {file_name}")
        case '2':
            file_name = input("Enter file name for JSON (e.g., visitors_data.json): ")
            df.to_json(file_name)
            print(f"Data successfully exported as {file_name}")
        case '3':
            print("Export canceled.")
        case _:
            print("Invalid choice. Please try again.")


# === Interactive Menu with match-case ===
def main_menu():
    # Generate the data
    df = generate_data()
    
    while True:
        # Display the menu options
        print("\n--- MENU ---")
        print("1. Monthly Analysis (mean and standard deviation)")
        print("2. Daily Visitors with 7-Day Moving Average")
        print("3. Monthly Average Visitors Plot")
        print("4. Export Data (CSV or JSON)")
        print("5. Exit")

        # Get user input for menu selection
        choice = input("Choose an option (1/2/3/4/5): ")
        
        # Use match-case for menu handling
        match choice:
            case '1':
                analyze_data(df)
            case '2':
                plot_daily_visitors(df)
            case '3':
                plot_monthly_averages(df)
            case '4':
                export_data(df)
            case '5':
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")


# === Program Execution ===
if __name__ == "__main__":
    main_menu()
