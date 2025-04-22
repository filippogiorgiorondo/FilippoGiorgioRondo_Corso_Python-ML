from db_utils import AnalisiUniversitaria, connects

"""
Andare a creare un piccolo sistema di analisi dei dati su un DB relazionale che deve essere generato
e collegare almeno 3 tabelle.
Ci dev’essere un menu per eseguire le principali funzioni che hai studiato con numpy.

"""
# === Funzione che funge da menù === 
def analisi_menu():
    analisi = AnalisiUniversitaria()

    # === Funzione fornire le info sui corsi ===
    def get_corsi():
        query = "SELECT id_corso, nome_corso FROM Corsi"
        with connects() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()

    # === Funzione fornire le info sugli studenti ===
    def get_studenti():
        query = "SELECT id_studente, nome_studente FROM Studenti"
        with connects() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()

    # === Ciclo per reiterare il menù ===
    while True:
        corsi = get_corsi()
        studenti = get_studenti()

        print("\n--- Corsi Disponibili ---")
        for corso in corsi:
            print(f"ID: {corso['id_corso']} - {corso['nome_corso']}")

        print("\n--- Studenti Iscritti ---")
        for studente in studenti:
            print(f"ID: {studente['id_studente']} - {studente['nome_studente']}")

        print("\n--- Menu Analisi ---")
        print("1. Media voti per corso")
        print("2. Deviazione standard voti studente")
        print("3. Mediana voti per corso")
        print("4. Somma voti studente")
        print("5. Voto min/max per corso")
        print("6. Numero esami studente")
        print("7. Distribuzione voti studente")
        print("8. Percentuale successo per corso")
        print("9. Esci")

        scelta = input("Scegli un'opzione (1-9): ").strip()

        try:
            match scelta:
                case "1":
                    corso_id = int(input("Inserisci ID corso: "))
                    media = analisi.media_voti_per_corso(corso_id)
                    print(f"Media voti corso {corso_id}: {media:.2f}" if media is not None else "Nessun voto disponibile.")
                case "2":
                    studente_id = int(input("Inserisci ID studente: "))
                    std = analisi.deviazione_stand_voti_studente(studente_id)
                    print(f"Deviazione standard voti studente {studente_id}: {std:.2f}" if std is not None else "Nessun voto disponibile.")
                case "3":
                    corso_id = int(input("Inserisci ID corso: "))
                    mediana = analisi.mediana_voti_corso(corso_id)
                    print(f"Mediana voti corso {corso_id}: {mediana}" if mediana is not None else "Nessun voto disponibile.")
                case "4":
                    studente_id = int(input("Inserisci ID studente: "))
                    somma = analisi.somma_voti_studente(studente_id)
                    print(f"Somma voti studente {studente_id}: {somma}")
                case "5":
                    corso_id = int(input("Inserisci ID corso: "))
                    minimo, massimo = analisi.voto_piu_basso_alto_corso(corso_id)
                    if minimo is None:
                        print("Nessun voto disponibile.")
                    else:
                        print(f"Voto più basso: {minimo}, Voto più alto: {massimo}")
                case "6":
                    studente_id = int(input("Inserisci ID studente: "))
                    count = analisi.numero_esami_studente(studente_id)
                    print(f"Numero di esami sostenuti da studente {studente_id}: {count}")
                case "7":
                    studente_id = int(input("Inserisci ID studente: "))
                    distribuzione = analisi.distribuzione_voti_studente(studente_id)
                    if distribuzione:
                        print("Distribuzione voti:")
                        for voto, occorrenze in sorted(distribuzione.items()):
                            print(f"  Voto {voto}: {occorrenze} volta(e)")
                    else:
                        print("Nessun voto disponibile.")
                case "8":
                    corso_id = int(input("Inserisci ID corso: "))
                    perc = analisi.percentuale_successo_corso(corso_id)
                    print(f"Percentuale di successo: {perc:.2f}%" if perc is not None else "Nessun voto disponibile.")
                case "9":
                    print("Uscita in corso... Grazie e arrivederci!")
                    break
                case _:
                    print("Scelta non valida. Riprova.")
        except ValueError:
            print("Errore: inserisci un ID numerico valido.")
        except Exception as e:
            print(f"Si è verificato un errore: {e}")

# === Esecuzione del codice ===
if __name__ == "__main__":
    analisi_menu()
