lista = []
print("La tua lista al momento è vuota (", lista, ")")
scelta = int(input("Se desideri aggiungere 3 numeri alla lista, premi 1. Altrimenti, premi 2")) #l'input viene trasformato in un numero intero

#blocco condizione if-elif-else per gestire l'input
if scelta == 1: 
    n1 = input("Inserisci il primo numero")
    lista.append(n1) #viene aggiunto il numero alla lista
    print("Numero aggiunto con successo")
    
    n2 = input("Inserisci il secondo numero")
    lista.append(n2) #viene aggiunto il numero alla lista
    print("Numero aggiunto con successo")
    
    n3 = input("Inserisci il terzo numero")
    lista.append(n3) #viene aggiunto il numero alla lista
    print("Numero aggiunto con successo")

elif scelta ==2:
    print("Chiusura del programma...")

else:
    print("Non hai premuto uno dei due tasti proposti, il programma viene interrotto")
    
###

print("Perfetto, adesso la tua lista non è più vuota (", lista, ")")
#richiede all'utente cosa fare con la lista mostrata
scelta = int(input("Premere 1 per aggiungere un elemento alla lista, premere 2 per togliere un elemento dalla lista, premere 3 per visualizzare la lista"))

if scelta == 1:
    n1 = int(input("Inserisci il numero da aggiungere")) #richiede all'utente di fornire il numero da aggiungere alla lista
    if n1 in lista:
        print("Numero già presente nella lista")
    else:
        lista.append(n1) #codice per aggiungere un elemento alla lista
        print("Il tuo numero è stato aggiunto con successo")
        print(lista, "Questa è la lista")

elif scelta == 2:
    n1 = int(input("Inserisci il numero da rimuovere: ")) #richiede all'utente di fornire il numero da rimuovere dalla lista
    if n1 in lista: #verifica che il numero inserito sia già lista
        print("Numero non presente nella lista")
    else:
        lista.remove(n1) #codice per rimuovere un numero specifico
        print("Il numero è stato rimosso con successo", lista)

elif scelta == 3:
    print("Ecco la tua lista", lista) #stampa la lista
    
else:
    print("Non hai scelto un numero corretto.. Chiusura programma")