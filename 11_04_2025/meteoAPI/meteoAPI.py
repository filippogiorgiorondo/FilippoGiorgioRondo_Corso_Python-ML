import requests  # Libreria per fare richieste HTTP (usata per chiamare le API)

# Funzione per ottenere latitudine e longitudine di una città usando l'API di geocoding
def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)  # Richiesta HTTP all'API
    data = response.json()        # Converte la risposta JSON in un dizionario Python

    # Se ci sono risultati, prendi il primo e restituisci latitudine e longitudine
    if data.get("results"):
        location = data["results"][0]
        return location["latitude"], location["longitude"]
    else:
        print("Città non trovata.")
        return None, None

# Funzione per ottenere il meteo da Open-Meteo in base alle coordinate, ai giorni e alle opzioni selezionate
def get_weather(lat, lon, days, show_wind, show_precipitation):
    # Costruzione dell'URL con i parametri obbligatori
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min"
    )

    # Aggiunge i dati opzionali all'URL se richiesti
    if show_wind:
        url += ",windspeed_10m_max"
    if show_precipitation:
        url += ",precipitation_sum"

    url += f"&forecast_days={days}&timezone=auto"  # Aggiunge il numero di giorni richiesto

    response = requests.get(url)  # Richiesta all’API del meteo
    return response.json()        # Restituisce i dati come dizionario

# Funzione per stampare il meteo giorno per giorno in modo leggibile
def mostra_meteo(meteo, giorni, show_wind, show_precipitation):
    daily = meteo["daily"]  # Accede alla sezione 'daily' dei dati meteo
    for i in range(giorni):
        print(f"\n📅 Giorno {i+1} ({daily['time'][i]}):")
        print(f"🌡 Temperatura max: {daily['temperature_2m_max'][i]}°C")
        print(f"🌡 Temperatura min: {daily['temperature_2m_min'][i]}°C")
        if show_wind:
            print(f"💨 Vento max: {daily['windspeed_10m_max'][i]} km/h")
        if show_precipitation:
            print(f"🌧 Precipitazioni: {daily['precipitation_sum'][i]} mm")

# Funzione principale che guida l’interazione con l’utente
def main():
    city = input("Inserisci il nome della città: ").strip()  # Richiede il nome della città
    lat, lon = get_coordinates(city)  # Ottiene le coordinate geografiche

    if lat is None or lon is None:  # Se la città non è stata trovata, termina
        return

    # Chiede all'utente per quanti giorni vuole il meteo (solo 1, 3 o 7 sono validi)
    while True:
        try:
            giorni = int(input("Vuoi il meteo per quanti giorni? (1, 3, 7): "))
            if giorni in (1, 3, 7):
                break
            else:
                print("Inserisci solo 1, 3 o 7.")
        except ValueError:
            print("Inserisci un numero valido.")

    # Chiede se si vogliono vedere vento e precipitazioni
    wind = input("Vuoi visualizzare anche la velocità del vento? (s/n): ").strip().lower() == "s"
    rain = input("Vuoi visualizzare anche le precipitazioni? (s/n): ").strip().lower() == "s"

    meteo = get_weather(lat, lon, giorni, wind, rain)  # Ottiene i dati meteo in base alle scelte

    if "daily" in meteo:  # Se la risposta contiene i dati giornalieri
        mostra_meteo(meteo, giorni, wind, rain)  # Stampa le informazioni
    else:
        print("Errore nel recupero dei dati meteo.")

# Punto d’ingresso dello script
if __name__ == "__main__":
    main()
