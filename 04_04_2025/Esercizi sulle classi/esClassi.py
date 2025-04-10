class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        if profitto == 0:
            print("Il seguente prodotto non offre alcun guadagno")
        
        elif profitto < 0:
            print(f"I costi di produzione sono maggiori del prezzo di vendita. La produzione costa {abs(profitto)} $ in più")
        else:
            print(f"Il profitto del prodotto è di {profitto}$")
    
class Fabbrica:
    def __init__(self):
        self.inventario = {
            "bmw-1X3":10,
            "fiat panda": 3,
            "mercedes benz-32": 5,
            "Toyota Hybrid 93": 9,
        }
        
        
    def aggiungi_prodotto(self):
        nomeAuto = input("Inserisci il nome dell'auto da aggiungere all'inventario: ")
        numeroAuto = int(input("Inserisci il numero di auto da aggiungere all'inventario: "))
       
        if nomeAuto in self.inventario: # Se l'auto da aggiungere è gia presente ne incrementa il valore, altrimenti aggiunge l'elemento al dizionario
            self.inventario[nomeAuto] += numeroAuto
        else:
            self.inventario[nomeAuto]  = [numeroAuto]
            costo_produzione = int(input("Inserisci il costro di produzione per una di queste auto"))
            prezzo_vendita=int(input("Inserisci il prezzo di vendita di una di queste macchine: "))
            nomeAuto = Prodotto(nomeAuto, costo_produzione, prezzo_vendita)    
    
    def vendi_prodotto(self):
        nomeAuto = input("Inserisci il nome dell'auto da vendere: ")
        numeroAuto = int(input("Inserisci il numero di auto da vendere: "))
       
        if nomeAuto in self.inventario: # presente ne incrementa il valore, altrimenti aggiunge l'elemento al dizionario
            if self.inventario[nomeAuto] -numeroAuto >= 0:
                print("Auto vendute con successo")
                self.inventario[nomeAuto] -= numeroAuto
                guadagno = nomeAuto.profitto * numeroAuto
                print(f"Il tuo guadagno è: {guadagno}")
            else:
                print("Auto non disponibili")
            
    def resi_prodotto(self):
        nomeAuto = input("Inserisci il nome dell'auto restituita")
        if nomeAuto in self.inventario: # Se l'auto da aggiungere è gia presente ne incrementa il valore, altrimenti aggiunge l'elemento al dizionario
            self.inventario[nomeAuto] += 1
        else:
            self.inventario[nomeAuto]  = [1]
            
f = Fabbrica()
while True:
   whatdo=int(input("Cosa vuole fare?\nAggiungere un'auto all'inventario(1)\nVendere un prodotto(2)\nEffettuare il reso di un'auto\nChiudere il programma(4)\n"))
   match whatdo:
        case 1:
           f.aggiungi_prodotto()
        case 2:
            f.vendi_prodotto()
        case 3:
            f.resi_prodotto()
        case 4:
            break
        case _:
            break