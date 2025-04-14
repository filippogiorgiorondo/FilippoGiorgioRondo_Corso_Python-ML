import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="partita_calcio"
    )

def crea_tabelle_database():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS allenatori (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50),
        eta INT,
        esperienza INT,
        bonus_attacco INT,
        bonus_difesa INT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS giocatori (
        numero_maglia INT PRIMARY KEY,
        nome VARCHAR(50),
        eta INT,
        ruolo VARCHAR(20),
        valore_attacco INT,
        valore_difesa INT,
        squadra VARCHAR(50)
    )
    """)

    conn.commit()
    conn.close()


def salva_allenatore(allenatore):
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    INSERT INTO allenatori (nome, eta, esperienza, bonus_attacco, bonus_difesa)
    VALUES (%s, %s, %s, %s, %s)
    """, (allenatore.nome, allenatore.eta, allenatore.anni_di_esperienza,
          allenatore.bonus_attacco, allenatore.bonus_difesa))

    conn.commit()
    conn.close()
    
    
def salva_giocatori(squadra, nome_squadra):
    conn = get_connection()
    c = conn.cursor()

    for g in squadra:
        c.execute("""
        INSERT INTO giocatori (numero_maglia, nome, eta, ruolo, valore_attacco, valore_difesa, squadra)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (g.numero_maglia, g.nome, g.eta, g.ruolo,
              g.valore_attacco, g.valore_difesa, nome_squadra))

    conn.commit()
    conn.close()
