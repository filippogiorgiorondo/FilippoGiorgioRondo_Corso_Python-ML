"""creare una classe base MetodoPagamento e diverse classi derivate che rappresentano
diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in
azione, permettendo alle diverse sottoclassi di implementare i loro specifici
comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe
base.



Classe MetodoPagamento:
Metodi:
effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
Classi Derivate:
CartaDiCredito:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta
di credito.
PayPal:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
BonificoBancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite
bonifico bancario.
GestorePagamenti:
Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza
preoccuparsi del dettaglio del metodo di pagamento."""

# Classe base
class MetodoPagamento:
    def effettua_pagamento(self, importo):
        pass

# Sottoclasse: Carta di Credito
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato con Carta di Credito.")

# Sottoclasse: PayPal
class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato tramite PayPal.")

# Sottoclasse: Bonifico Bancario
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato tramite Bonifico Bancario.")

# Classe che usa il metodo di pagamento in modo polimorfico
class GestorePagamenti:
    def __init__(self, metodo: MetodoPagamento): # type hinting, indica che ci si aspetta che metodo sia oggetto MetodoDiPagamento o una sua sottoclasse
        self.metodo = metodo

    def paga(self, importo):
        self.metodo.effettua_pagamento(importo)
        
# Creo i metodi di pagamento
carta = CartaDiCredito()
paypal = PayPal()
bonifico = BonificoBancario()

# Creo gestori con metodi diversi
gestore1 = GestorePagamenti(carta)
gestore2 = GestorePagamenti(paypal)
gestore3 = GestorePagamenti(bonifico)

# Eseguo i pagamenti (tutti usano lo stesso metodo paga())
gestore1.paga(100.50)  # Carta
gestore2.paga(25.75)   # PayPal
gestore3.paga(300.00)  # Bonifico

