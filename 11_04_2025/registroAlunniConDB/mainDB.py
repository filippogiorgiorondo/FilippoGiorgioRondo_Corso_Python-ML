from db_utils import *

# === Funzione per il menu principale ===
def menu_principale():
    print("\n--- MENU ---")
    print("1. Aggiungi alunno")
    print("2. Mostra registro alunni")
    print("3. Modifica voti alunno")
    print("4. Elimina alunno")
    print("5. Esci")
    
# === Funzione principale ===
def main():
    
    # === Connessione al DB ===
    while True:
        try:
            conn = connect_to_db()
            print("Connessione al DB aperta")
            break
        except:
            print("Problemi di connessione")
            scelta = input("Vuoi riprovare a connetterti al DB (s/n)").lower()
            if scelta != "s":
                quit
                
    # === Creazione della tabella se non esiste ===
    cursor = open_cursor(conn)
    create_table(cursor)
    print("La tabella è creata (o esisteva già)")
    
    while True:
        menu_principale()
        scelta = input("Scegli un'opzione: ")
        cursor = open_cursor(conn)
        match scelta:
            case "1":
          
                # === Aggiungi un alunno ===
                nome = input("Inserisci il nome dell'alunno: ").strip()
                cognome = input("Inserisci il cognome dell'alunno: ").strip()
                numero_voti = int(input("Inserisci il numero di voti da aggiungere:"))
                voti = [int(input(f"Inserisci voto {i+1}: ")) for i in range(numero_voti)]
                
                if add_student(cursor, nome, cognome, voti):
                    print(f"L'alunno {nome} {cognome} è stato aggiunto con successo")
                else:
                    print(f"L'alunno {nome} {cognome} è gia presente nel database")
            
            case "2":

                # === Mostra tutti gli alunni ===
                show_students(cursor)
                
                # Chiedese l'utente vuole visualizzare un alunno specifico
                scelta_specifico = input("\nVuoi vedere i dettagli di un alunno specifico? (s/n): ").strip().lower()

                if scelta_specifico == "s":
                    # Chiede l'ID dell'alunno da visualizzare
                    alunno_id = int(input("Inserisci l'ID dell'alunno: "))
                    show_single_student(cursor, alunno_id)
                
            case "3":
                alunno_id = int(input("Inserisci l'ID dell'alunno per modificare i voti: "))
                
                # === Modifica dei voti ===
                modify_student_vote(cursor, alunno_id)

            case "4":

                # Chiede l'ID dell'alunno da eliminare
                alunno_id = int(input("Inserisci l'ID dell'alunno da rimuovere"))
                
                # === Elimina alunno
                delete_student(cursor, alunno_id)
            
            case "5":
                print("Uscita dal programma")
                break
                
            case _:
                print("Scelta non valida, uscita dal programma")
                break
                
        cursor.close()
    conn.close()

main()
