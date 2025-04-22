import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager
import numpy as np
# CONFIGURAZIONE PER LA CONNESSIONE AL DB
db_conf = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'università'
}

# Dati fittizi per i corsi
corsi = [
    {"nome_corso": "Matematica", "codice_corso": "MATH101"},
    {"nome_corso": "Informatica", "codice_corso": "INF102"},
    {"nome_corso": "Fisica", "codice_corso": "PHYS103"}
]

esami = [
    {"nome_corso": "Matematica", "nome_esame": "Esame di Matematica", "data_esame": "2025-06-01"},
    {"nome_corso": "Informatica", "nome_esame": "Esame di Informatica", "data_esame": "2025-06-05"},
    {"nome_corso": "Fisica", "nome_esame": "Esame di Fisica", "data_esame": "2025-06-10"}
]

studenti = [
    {"nome_studente": "Mario Rossi"},
    {"nome_studente": "Luca Bianchi"},
    {"nome_studente": "Anna Verdi"},
    {"nome_studente": "Giulia Ferri"},
    {"nome_studente": "Matteo Galli"},
    {"nome_studente": "Elena Martino"},
    {"nome_studente": "Francesco Mancini"},
    {"nome_studente": "Sara Russo"},
    {"nome_studente": "Alessandro Perri"},
    {"nome_studente": "Valentina Moretti"},
    {"nome_studente": "Carlo Santoro"},
    {"nome_studente": "Federica Giordano"},
    {"nome_studente": "Andrea Conti"},
    {"nome_studente": "Vincenzo Longo"},
    {"nome_studente": "Chiara Bellini"}
]

risultati_esame = [
    {"nome_esame": "Esame di Matematica", "nome_studente": "Mario Rossi", "nome_corso": "Matematica", "voto": 28},
    {"nome_esame": "Esame di Matematica", "nome_studente": "Luca Bianchi", "nome_corso": "Matematica", "voto": 30},
    {"nome_esame": "Esame di Matematica", "nome_studente": "Anna Verdi", "nome_corso": "Matematica", "voto": 25},
    {"nome_esame": "Esame di Informatica", "nome_studente": "Mario Rossi", "nome_corso": "Informatica", "voto": 24},
    {"nome_esame": "Esame di Informatica", "nome_studente": "Luca Bianchi", "nome_corso": "Informatica", "voto": 29},
    {"nome_esame": "Esame di Informatica", "nome_studente": "Giulia Ferri", "nome_corso": "Informatica", "voto": 21},
    {"nome_esame": "Esame di Fisica", "nome_studente": "Anna Verdi", "nome_corso": "Fisica", "voto": 28},
    {"nome_esame": "Esame di Fisica", "nome_studente": "Matteo Galli", "nome_corso": "Fisica", "voto": 30},
    {"nome_esame": "Esame di Fisica", "nome_studente": "Elena Martino", "nome_corso": "Fisica", "voto": 22},
    {"nome_esame": "Esame di Fisica", "nome_studente": "Francesco Mancini", "nome_corso": "Fisica", "voto": 26},
    {"nome_esame": "Esame di Fisica", "nome_studente": "Sara Russo", "nome_corso": "Fisica", "voto": 23},
    {"nome_esame": "Esame di Fisica", "nome_studente": "Alessandro Perri", "nome_corso": "Fisica", "voto": 27},
    {"nome_esame": "Esame di Informatica", "nome_studente": "Valentina Moretti", "nome_corso": "Informatica", "voto": 20},
    {"nome_esame": "Esame di Matematica", "nome_studente": "Federica Giordano", "nome_corso": "Matematica", "voto": 26}
]

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
            
class AnalisiUniversitaria:
    def __init__(self):
        pass  # Connessione gestita con `with`

    def get_all_results(self):
        query = """
            SELECT RE.voto, RE.id_studente, E.id AS id_esame, C.id_corso
            FROM Risultati_Esame RE
            JOIN Esami E ON RE.id_esame = E.id
            JOIN Corsi C ON E.id_corso = C.id_corso
        """
        with connects() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()

    def media_voti_per_corso(self, corso_id):
        results = self.get_all_results()
        voti = [r['voto'] for r in results if r['id_corso'] == corso_id]
        return np.mean(voti) if voti else None

    def deviazione_stand_voti_studente(self, studente_id):
        results = self.get_all_results()
        voti = [r['voto'] for r in results if r['id_studente'] == studente_id]
        return np.std(voti) if voti else None

    def mediana_voti_corso(self, corso_id):
        results = self.get_all_results()
        voti = [r['voto'] for r in results if r['id_corso'] == corso_id]
        return np.median(voti) if voti else None

    def somma_voti_studente(self, studente_id):
        results = self.get_all_results()
        voti = [r['voto'] for r in results if r['id_studente'] == studente_id]
        return np.sum(voti) if voti else 0

    def voto_piu_basso_alto_corso(self, corso_id):
        results = self.get_all_results()
        voti = [r['voto'] for r in results if r['id_corso'] == corso_id]
        return (np.min(voti), np.max(voti)) if voti else (None, None)

    def numero_esami_studente(self, studente_id):
        results = self.get_all_results()
        return len([r for r in results if r['id_studente'] == studente_id])

    def distribuzione_voti_studente(self, studente_id):
        results = self.get_all_results()
        voti = [r['voto'] for r in results if r['id_studente'] == studente_id]
        unique, counts = np.unique(voti, return_counts=True)
        return dict(zip(unique, counts))

    def percentuale_successo_corso(self, corso_id):
        results = self.get_all_results()
        voti = [r['voto'] for r in results if r['id_corso'] == corso_id]
        if not voti:
            return None
        successi = [v for v in voti if v >= 18]
        return round(len(successi) / len(voti) * 100, 2)



