import random
import salvataggiDB

# === CLASSI BASE ===

class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def descrivi(self):
        return f"{self.nome}, età {self.eta}"

class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia, valore_attacco=0, valore_difesa=0):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        self.valore_attacco = valore_attacco
        self.valore_difesa = valore_difesa
        self.gol_segnati = 0

    def gioca_partita(self):
        return f"{self.nome} gioca come {self.ruolo}."

class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza
        self.bonus_attacco = 0
        self.bonus_difesa = 0

    def assegna_bonus(self, bonus_attacco, bonus_difesa):
        totale = bonus_attacco + bonus_difesa
        if totale > 5:
            raise ValueError("Puoi assegnare al massimo 5 punti bonus in totale.")
        self.bonus_attacco = bonus_attacco
        self.bonus_difesa = bonus_difesa

    def gestisci_squadra(self, giocatori):
        for giocatore in giocatori:
            if giocatore.ruolo == "attaccante":
                giocatore.valore_attacco += self.bonus_attacco
            elif giocatore.ruolo == "difensore":
                giocatore.valore_difesa += self.bonus_difesa

# === MENU CREAZIONE SQUADRA ===

def menu_creazione_squadra():
    squadra = []
    numeri_assegnati = set()

    print("=== CREAZIONE SQUADRA ===")
    nome_allenatore = input("Nome dell'allenatore: ")
    eta_allenatore = int(input("Età dell'allenatore: "))
    esperienza = int(input("Anni di esperienza dell'allenatore: "))
    nome_squadra = input("Nome della tua squadra: ")
    allenatore = Allenatore(nome_allenatore, eta_allenatore, esperienza)

    punti_totali = 100
    print(f"\nHai {punti_totali} punti totali da distribuire tra ATTACCO e DIFESA.")

    num_attaccanti = int(input("\nQuanti attaccanti vuoi (max 4)? "))
    num_difensori = 4 - num_attaccanti
    num_portieri = 1

    def chiedi_numero_maglia():
        while True:
            numero = random.randint(1, 99)
            if numero not in numeri_assegnati:
                numeri_assegnati.add(numero)
                return numero

    for i in range(num_attaccanti):
        print(f"\n== Attaccante {i+1} ==")
        nome = input("Nome: ")
        eta = int(input("Età: "))
        numero_maglia = chiedi_numero_maglia()
        print(f"Numero maglia assegnato: {numero_maglia}")
        att = int(input("Punti ATTACCO: "))
        dif = 0
        if att + dif > punti_totali:
            print("Hai superato i punti disponibili. Riprova.")
            return menu_creazione_squadra()
        punti_totali -= (att + dif)
        squadra.append(Giocatore(nome, eta, "attaccante", numero_maglia, att, dif))

    for i in range(num_difensori):
        print(f"\n== Difensore {i+1} ==")
        nome = input("Nome: ")
        eta = int(input("Età: "))
        numero_maglia = chiedi_numero_maglia()
        print(f"Numero maglia assegnato: {numero_maglia}")
        att = int(input("Punti ATTACCO: "))
        dif = int(input("Punti DIFESA: "))
        if att + dif > punti_totali:
            print("Hai superato i punti disponibili. Riprova.")
            return menu_creazione_squadra()
        punti_totali -= (att + dif)
        squadra.append(Giocatore(nome, eta, "difensore", numero_maglia, att, dif))

    print(f"\n== Portiere ==")
    nome = input("Nome: ")
    eta = int(input("Età: "))
    numero_maglia = chiedi_numero_maglia()
    print(f"Numero maglia assegnato: {numero_maglia}")
    att = int(input("Punti ATTACCO: "))
    dif = int(input("Punti DIFESA: "))
    if att + dif > punti_totali:
        print("Hai superato i punti disponibili. Riprova.")
        return menu_creazione_squadra()
    squadra.append(Giocatore(nome, eta, "portiere", numero_maglia, att, dif))
    punti_totali -= (att + dif)

    print(f"\nHai completato la squadra! Punti rimanenti: {punti_totali}")

    # Bonus allenatore
    print("\nOra puoi assegnare i 5 punti bonus dell'allenatore.")
    while True:
        try:
            bonus_att = int(input("Punti bonus ATTACCO: "))
            bonus_dif = int(input("Punti bonus DIFESA: "))
            allenatore.assegna_bonus(bonus_att, bonus_dif)
            break
        except ValueError as e:
            print(e)

    allenatore.gestisci_squadra(squadra)

    # Riepilogo
    print("\n--- RIEPILOGO SQUADRA ---")
    print("Allenatore:", allenatore.descrivi())
    print(f"Bonus Attacco: {allenatore.bonus_attacco}, Bonus Difesa: {allenatore.bonus_difesa}")
    print("Giocatori:")
    for g in squadra:
        print(f"Maglia {g.numero_maglia} - {g.nome} ({g.ruolo}) | Att: {g.valore_attacco} | Dif: {g.valore_difesa}")

    # Salvataggio nel database
    salvataggiDB.salva_allenatore(allenatore)
    salvataggiDB.salva_giocatori(squadra, nome_squadra)

    return allenatore, squadra

# === GENERAZIONE SQUADRA AVVERSARIA ===

def genera_squadra_avversaria():
    squadra = []
    numeri_maglia = set()
    nome_squadra = "Squadra Avversaria"

    def genera_numero_maglia():
        while True:
            numero = random.randint(1, 99)
            if numero not in numeri_maglia:
                numeri_maglia.add(numero)
                return numero

    num_attaccanti = random.randint(1, 3)
    num_difensori = 4 - num_attaccanti
    nomi = ["Alex", "Luca", "Marco", "Fede", "Leo", "Tom", "Vale", "Gio", "Miki", "Ricky"]

    for _ in range(num_attaccanti):
        nome = random.choice(nomi)
        eta = random.randint(18, 35)
        numero_maglia = genera_numero_maglia()
        valore_attacco = random.randint(10, 25)
        valore_difesa = 0
        squadra.append(Giocatore(nome, eta, "attaccante", numero_maglia, valore_attacco, valore_difesa))

    for _ in range(num_difensori):
        nome = random.choice(nomi)
        eta = random.randint(18, 35)
        numero_maglia = genera_numero_maglia()
        valore_attacco = random.randint(5, 15)
        valore_difesa = random.randint(10, 25)
        squadra.append(Giocatore(nome, eta, "difensore", numero_maglia, valore_attacco, valore_difesa))

    nome = random.choice(nomi)
    eta = random.randint(20, 38)
    numero_maglia = genera_numero_maglia()
    valore_attacco = random.randint(1, 5)
    valore_difesa = random.randint(15, 30)
    squadra.append(Giocatore(nome, eta, "portiere", numero_maglia, valore_attacco, valore_difesa))

    print("\n--- Squadra Avversaria Generata ---")
    for g in squadra:
        print(f"Maglia {g.numero_maglia} - {g.nome} ({g.ruolo}) | Att: {g.valore_attacco} | Dif: {g.valore_difesa}")

    # Salvataggio nel database
    salvataggiDB.salva_giocatori(squadra, nome_squadra)

    return squadra

# === ESECUZIONE ===

salvataggiDB.crea_tabelle_database()
menu_creazione_squadra()
genera_squadra_avversaria()