import mysql.connector

# === Connessione al database ===
def connect_to_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      
        database="testdb"
    )
    return conn

# === Crea cursore da connessione ===
def open_cursor(conn):
    return conn.cursor()

# === Chiude il cursore da connessione ===
def close_cursor(cursor):
    cursor.close()

# === Crea la tabella 'alunni' se non esiste ===
def create_table(cursor):
    query = """
    CREATE TABLE IF NOT EXISTS alunni (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50),
        cognome VARCHAR(50),
        voti TEXT,
        media FLOAT
    );
    """
    cursor.execute(query)
    
# === Calcola la media prima di aggiungerla al DB
def student_average(voti):
    return round(sum(voti) / len(voti) if len(voti) > 0 else 0,2) # Restituisce la media arrotondata di 2
    
# === Aggiunge l'alunno al DB ===
def add_student(cursor, nome, cognome, voti):
    cursor.execute("SELECT * FROM alunni WHERE nome=%s AND cognome=%s", (nome, cognome))
    if cursor.fetchone():# restituisce la prima riga se trovata
        print(f"L'alunno {nome} {cognome} è già presente nel DB")
        return False
    
    media = student_average(voti) # Calcolo della media
    voti_str = "-".join(map(str, voti)) # converte i voti in formato stringa (es: 1-3-2)
    
 # Inserisce il nuovo alunno nel database
    cursor.execute(
        "INSERT INTO alunni (nome, cognome, voti, media) VALUES (%s, %s, %s, %s)",
        (nome, cognome, voti_str, media)
    )
    return True  # Se l'inserimento è avvenuto correttamente, ritorna True

# === Mostra alunni ===
def show_students(cursor):
    cursor.execute("SELECT id, nome, cognome FROM alunni") # Mostra tutti gli alunni senza voti
    alunni = cursor.fetchall() # ottiene tutte le righe
    if not alunni:
        print("Nessun alunno presente nel DB")
    else:
        print("\n--- Elenco Alunni ---")
        for alunno in alunni:
            # Mostra id, nome e cognome per ogni alunno
            print(f"ID: {alunno[0]}, Nome: {alunno[1]}, Cognome: {alunno[2]}")
            
# === Mostra un solo alunno ===
def show_single_student(cursor, alunno_id):
    cursor.execute("SELECT * FROM alunni WHERE id=%s", (alunno_id,))
    alunno = cursor.fetchone()

    if alunno: # Se l'alunno viene trovato ne stampa i dati
        print("\n--- Dettagli Alunno ---")
        print(f"ID: {alunno[0]}")
        print(f"Nome: {alunno[1]}")
        print(f"Cognome: {alunno[2]}")
        print(f"Voti: {alunno[3]}")
        print(f"Media: {alunno[4]}")
    else:
        print(f"L'alunno con ID {alunno_id} non è stato trovato nel database.")

# === Modifica uno o più voti o tutti i voti ===
def modify_student_vote(cursor, alunno_id):
        
    # Recupera i voti attuali dell'alunno
    cursor.execute("SELECT nome, cognome, voti FROM alunni WHERE id=%s", (alunno_id,))
    alunno = cursor.fetchone()  # Recupera la singola riga

    if not alunno:  # Verifica che l'alunno esiste nel DB
        print(f"L'alunno con ID {alunno_id} non è stato trovato nel database.")
        return

    # Mostra i voti attuali
    nome, cognome, voti_str = alunno
    voti = list(map(int, voti_str.split("-")))  # Converte la stringa in lista di interi
    print(f"\nVoti attuali per {nome} {cognome}: {voti_str}")

    # Chiedecosa vuole fare l'utente
    print("\nOpzioni disponibili:")
    print("1. Modifica un voto")
    print("2. Rimuovi un voto")
    print("3. Modifica più voti")
    print("4. Rimuovi più voti")
    
    scelta = input("Scegli un'opzione (1, 2, 3, 4): ").strip()

    match scelta:
        case "1":
            # Modifica un singolo voto
            voto_da_modificare = int(input(f"Quale voto vuoi modificare? Voti attuali: {voti}. Inserisci un voto: "))
            
            if voto_da_modificare not in voti:
                print(f"Il voto {voto_da_modificare} non è presente nei voti dell'alunno.")
                return

            nuovo_voto = int(input(f"Inserisci il nuovo voto per {voto_da_modificare}: "))
            
            # Modifica il voto nella lista
            for i in range(len(voti)):
                if voti[i] == voto_da_modificare:
                    voti[i] = nuovo_voto
                    break

        case "2":
            # Rimuove un singolo voto
            voto_da_rimuovere = int(input(f"Quale voto vuoi rimuovere? Voti attuali: {voti}. Inserisci un voto: "))
            
            if voto_da_rimuovere not in voti:
                print(f"Il voto {voto_da_rimuovere} non è presente nei voti dell'alunno.")
                return

            # Rimuove il voto dalla lista
            voti.remove(voto_da_rimuovere)

        case "3":
            # Modifica più voti
            print(f"I voti attuali: {voti}")
            voti_da_modificare = input("Inserisci i voti da modificare separati da virgola (es: 6,7): ").split(",")
            voti_da_modificare = list(map(int, voti_da_modificare))

            for voto in voti_da_modificare:
                if voto in voti:
                    nuovo_voto = int(input(f"Inserisci il nuovo voto per {voto}: "))
                    for i in range(len(voti)):
                        if voti[i] == voto:
                            voti[i] = nuovo_voto
                            break
                else:
                    print(f"Il voto {voto} non è presente tra i voti dell'alunno.")

        case "4":
            # Rimuove più voti
            print(f"I voti attuali: {voti}")
            voti_da_rimuovere = input("Inserisci i voti da rimuovere separati da virgola (es: 6,7): ").split(",")
            voti_da_rimuovere = list(map(int, voti_da_rimuovere))

            for voto in voti_da_rimuovere:
                if voto in voti:
                    voti.remove(voto)
                else:
                    print(f"Il voto {voto} non è presente tra i voti dell'alunno.")

        case "5":
            print("Scelta non valida.")
            return

    # Ricalcola la media
    media = round(sum(voti) / len(voti), 2) if voti else 0.0  # Evita divisione per zero

    # Crea la nuova stringa dei voti
    voti_str_aggiornati = "-".join(map(str, voti))

    # Aggiorna il database con i nuovi voti e la nuova media
    cursor.execute(
        "UPDATE alunni SET voti=%s, media=%s WHERE id=%s",
        (voti_str_aggiornati, media, alunno_id)
         )
    print(f"Voti aggiornati per {nome} {cognome}. Nuova media: {media}")

def delete_student(cursor, alunno_id):
    cursor.execute("SELECT nome, cognome FROM alunni WHERE id=%s", (alunno_id))
    alunno = cursor.fetchone() # Recupera nome e cognome dell'alunno

    if not alunno:
        print(f"L'alunno con ID {alunno_id} non è presente nel registro")
    
    nome, cognome = alunno
    # Conferma eliminazione
    conferma = input(f"Sei sicuro di voler eliminare l'alunno {nome} {cognome}? (s/n): ").strip().lower()
    if conferma == 's':
        cursor.execute("DELETE FROM alunni WHERE id=%s", (alunno_id,))
        print(f"L'alunno {nome} {cognome} è stato eliminato dal database.")
    else:
        print("Operazione di eliminazione annullata.")