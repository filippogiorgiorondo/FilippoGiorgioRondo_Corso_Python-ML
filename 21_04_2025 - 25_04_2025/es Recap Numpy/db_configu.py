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
