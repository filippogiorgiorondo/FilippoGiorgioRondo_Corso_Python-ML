from configurazioni import db_conf
import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager

# === Funzione per collegarsi ad database ===
@contextmanager
def connects():
    """
    Context Manager per connettersi al database e gestire automaticamente la chiusura.
    """
    conn = None
    try:
        conn = mysql.connector.connect(
            host=db_conf['host'],
            user=db_conf['user'],
            password=db_conf['password'],
            database=db_conf['database']
        )
        if conn.is_connected():
            print("Connessione al database riuscita.")
            yield conn
        else:
            raise Error("Connessione fallita.")
    except Error as err:
        print(f"Errore nella connessione: {err}")
        raise  # rilancia l’eccezione per gestirla fuori se serve
    finally:
        if conn and conn.is_connected():
            conn.close()
            print("Connessione chiusa.")

# === Funzione per creare le tabelle ===
def create_tables():
    with connects() as conn:
        if conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Studenti (
                    id_studente INT AUTO_INCREMENT PRIMARY KEY,
                    nome_studente VARCHAR(255) NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Corsi (
                    id_corso INT AUTO_INCREMENT PRIMARY KEY,
                    nome_corso VARCHAR(255) NOT NULL,
                    codice_corso VARCHAR(20) NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Esami (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    id_corso INT,
                    nome_esame VARCHAR(255),
                    data_esame DATE,
                    FOREIGN KEY (id_corso) REFERENCES Corsi(id_corso)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Risultati_Esame (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    id_esame INT,
                    id_studente INT,
                    voto INT,
                    FOREIGN KEY (id_esame) REFERENCES Esami(id),
                    FOREIGN KEY (id_studente) REFERENCES Studenti(id_studente)
                )
            """)

            conn.commit()
            print("Tabelle create con successo")

# === Funzione per popolare le tabelle nel database Università ===
def populate_universita_tables(studenti, corsi, esami, risultati_esame):
    try:
        with connects() as conn:
            if conn:
                cursor = conn.cursor()

                # Corsi
                for corso in corsi:
                    cursor.execute("""
                        INSERT INTO Corsi (nome_corso, codice_corso)
                        VALUES (%s, %s)
                    """, (corso['nome_corso'], corso['codice_corso']))

                # Studenti
                for studente in studenti:
                    cursor.execute("""
                        INSERT INTO Studenti (nome_studente)
                        VALUES (%s)
                    """, (studente['nome_studente'],))

                # Esami
                for esame in esami:
                    cursor.execute("""
                        SELECT id_corso FROM Corsi WHERE nome_corso = %s
                    """, (esame['nome_corso'],))
                    id_corso = cursor.fetchone()[0]

                    cursor.execute("""
                        INSERT INTO Esami (id_corso, nome_esame, data_esame)
                        VALUES (%s, %s, %s)
                    """, (id_corso, esame['nome_esame'], esame['data_esame']))

                # Risultati Esame
                for risultato in risultati_esame:
                    # Recupera ID esame
                    cursor.execute("""
                        SELECT E.id FROM Esami E
                        JOIN Corsi C ON E.id_corso = C.id_corso
                        WHERE E.nome_esame = %s AND C.nome_corso = %s
                    """, (risultato['nome_esame'], risultato['nome_corso']))
                    id_esame = cursor.fetchone()[0]

                    # Recupera ID studente
                    cursor.execute("""
                        SELECT id_studente FROM Studenti WHERE nome_studente = %s
                    """, (risultato['nome_studente'],))
                    id_studente = cursor.fetchone()[0]

                    cursor.execute("""
                        INSERT INTO Risultati_Esame (id_esame, id_studente, voto)
                        VALUES (%s, %s, %s)
                    """, (id_esame, id_studente, risultato['voto']))

                conn.commit()
                print("Tabelle Università popolate con successo!")

    except Exception as e:
        print(f"Errore durante l'inserimento: {e}")

# === Richiamo la funzione per creare le tabelle
# create_tables()

# === Richiamo la funzione per popolare le tabelle ===
# populate_universita_tables(studenti, corsi, esami, risultati_esame)
