# PYTHON
print("""
--PYTHON-- 
Python è un linguaggio programmazione fondato su un principio fondamentale: l'astrazione, ossia la capacità di dividere l'azione dal corpo di un elemento.
Altri tre concetti tecnici principali lo caratterizzano:incapsulamento, ereditarietà, polimorfismo.
- L'incapsulamento permette di nascondere i dettagli interni di una classe e proteggere i dati dall'accesso diretto dall'esterno. 
- L'ereditarietà è il meccanismo che permette a una classe (detta classe figlia) di ereditare attributi e metodi da un'altra classe (detta classe padre)
- Il polimorfismo permette di utilizzare lo stesso metodo su oggetti di classi diverse.

Per capirci, basti pensare alla funzione print.
print(1 + 1)
print("1" + "1")
- Quando viene richiamata la funzione, non vengono mostrati i dettagli complessi poichè sono intrinseci nel compilatore o nell'IDE -- Astrazione
- Il risultato che stampa print non è nient'altro che un 'figlio' --Ereditarietà
- Print funziona per ogni tipo di dato e può modificare gli strumenti utilizzati. Nell'esempio il '+' da operatore matematico diventa concatenatore di stringhe -- Polimorfismo
- L'incapsulamento protegge i dettagli interni di una classe e fornisce un'interfaccia pubblica sicura. -- Incapsulamento
    
Python è un linguaggio molto potente anche per altri motivi: è interpretato (prima di essere compilato controlla eventuali errori); è orientato agli oggetti (sfrutta i paradigmi OOP); è dinamico (nonostante sia fortemente tipizzato, permette una flessibilità dei dati)     
""")

# COMMENTI E I/O
print("""
Il codice scritto può essere commentato in modo da ricordare a noi stessi ciò che stiamo facendo e permettere ad un utente esterno di interpretare al meglio il codice

Interazione programma utente: Il codice può effettuare stampe a schermo (output) e interagire con l'utente chiedendogli di inserire dati o informazioni ad esempio tramite tastiera (input)       
    """)

# VARIABILI E TIPI DI DATO
print("""
Le variabili sono contenitori che possono memorizzare diversi tipi di dati, come numeri, testi e valori booleani. In Python, le variabili non hanno un tipo fisso, poiché Python è un linguaggio dinamicamente tipizzato: ciò significa che il tipo di dato viene assegnato automaticamente quando si assegna un valore alla variabile.
Ad una variabile è possibile attribuire nomi qualsiasi ma è consigliato contestualizzarlo in base alle necessità. Seguono alcuni vinconi per l'assegnazione del nome ad una variabile: non può iniziare per lettera maiuscola (altrimenti sarebbe una classe); non possono iniziare per numero; se iniziano con '_' vengono considerate variabili private e non direttamentea accessibili (è possibile accedervi mediante delle raggirazioni)

Una variabile, a differenza delle liste, può contenere solo un tipo di dato.
- Dati booleani = rappresentano valori logici True o False, sono molto importanti per i controllori del flusso e blocchi decisionali
- Dati numerici = Possono essere numeri interi, numeri in virgola mobile (int e float)
- Dati semantici = Qui troviamo le stringhe (str) che si specializzando in tipi speciali o composti poichè, a loro volta, sono costiti da una parte elementare detta 'char' 

Da questi tipi di dati ne derivano altrettanti, associabili alle variabili: liste, tuple, dizionari, insiemi.
La tipologia di dato della variabile non deve essere espressa poichè in python viene interpretata. E' possibile utilizzare la funzione type() per determinare il tipo di oggetto o variabile    
 
Funzioni Build-in Variabili:
str(var)	Converte in stringa	str(10) → "10"
int(var)	Converte in intero	int("5") → 5
float(var)	Converte in numero decimale	float("3.14") → 3.14
bool(var)	Converte in booleano	bool(0) → False
len(var)	Restituisce la lunghezza (funziona con stringhe, liste, tuple, ecc.)	len("ciao") → 4

Metodi per le stringhe:
.upper()	Converte in maiuscolo	"ciao".upper() → "CIAO"
.lower()	Converte in minuscolo	"CIAO".lower() → "ciao"
.capitalize()	Prima lettera maiuscola	"ciao".capitalize() → "Ciao"
.strip()	Rimuove spazi bianchi all'inizio e alla fine	" ciao ".strip() → "ciao"
.replace(a, b)	Sostituisce a con b	"hello".replace("h", "H") → "Hello """)

# LISTE E TUPLE
print("""
In Python, liste (tipologia: list) e tuple (tipologia: tuple) sono entrambi tipi di dati che permettono di memorizzare collezioni di elementi. Le prime vengono rappresentate con [] e le seconde con () 

--LISTE--
lista = [cane, 1, "pappagallo",33, True]
Caratteristiche principali:
- ordinate (seguono l'ordine con cui i dati sono aggiunti ad esse)
- al loro interno possono avere diversi tipi di dato
- indicizzate a partire a 0, ossia che il primo elemento della lista avrà indice 0, il secondo 1 e così via..
- supportano funzioni per essere manipolate   

Es Funzioni Build-in per le liste:
- len(lista)	Restituisce la lunghezza della lista	len([1, 2, 3]) → 3
- max(lista)	Restituisce il valore massimo (solo per liste numeriche o ordinate)	max([3, 7, 1]) → 7
- min(lista)	Restituisce il valore minimo	min([3, 7, 1]) → 1
- sum(lista)	Restituisce la somma degli elementi numerici	sum([1, 2, 3]) → 6
- sorted(lista)	Restituisce una nuova lista ordinata	sorted([3, 1, 4]) → [1, 3, 4]

Es metodi (funzioni associate ad un oggetto):
- append(x)	Aggiunge x alla fine della lista	[1, 2].append(3) → [1, 2, 3]
- remove(x)	Rimuove il primo elemento con valore x	[1, 2, 3].remove(2) → [1, 3]
- pop(i)	Rimuove l'elemento in posizione i e lo restituisce	[1, 2, 3].pop(1) → [1, 3]
- sort()	Ordina la lista in ordine crescente	[3, 1, 2].sort() → [1, 2, 3]
- sort(reverse=True)	Ordina la lista in ordine decrescente	[1, 2, 3].sort(reverse=True) → [3, 2, 1]
- everse()	Inverte l'ordine degli elementi	[1, 2, 3].reverse() → [3, 2, 1] 
      
--TUPLE--
tupla = (1,3,2,4)
Caratteristiche principale:
- una volta create non possono essere modificate a meno che non siano create vuote: tupla = ()
- non essendo modificabile non supporta funzioni o metodi   
      """)
      
#CONTROLLORI DEL FLUSSO
print("""
I controllori del flusso sono costrutti della programmazione che regolano l'esecuzione del codice in base a condizioni o iterazioni.
Si distinguono in: strutture condizionali e cicli.

--STRUTTURE CONDIZIONALI--
Le strutture condizionali sono i blocchi if-elif-else e match-case. Permettono di eseguire blocchi di codice in base a condizioni rispettate.
If ed else ecessitano obbligatoriamente di una condizione da verificare e questo processo può avere due soluzioni: Vero o False (True o False)

--IF-ELSE
es: if-elif-else
numero = 5
if numero == 5: #se il controllo restituisce True, esegue la condizione correlata
    print("Il numero è uguale a 5")
elif numero == 0: # se la condizione precedente restituisce false, viene fatto un ulteriore check
    print("Il numero è uguale a 0")
else: # se le prime due condizioni non vengono verificate, accade la condizine correlata
    print("Il numero non è nè uguale a 5 nè uguale a 0")
#output: "il numero è uguale a 5
In un blocco if-else, si può mettere un solo if (all'inizio) e un solo else (alla fine), al centro si possono mettere infiniti elif

--MATCH-CASE--
E' un costrutto simile allo switch-case in java, molto utile nelle sezioni menù e serve a verificare una scelta fornita
es: match-case
cosafare = "dormire"
match cosafare: # offre delle "casistiche" possibili che possono coincidere con la variabile passata (cosafare)
    case "dormire":
            print("Dormire")
    case "svegliarsi":
            print("Svegliarsi")
    case _:
    print("Altro") # caso di default, avviene quando non ci sono corrispondenze
    
--CICLI--
I cicli sono dei controllori del flusso che reiterano una determinata porzione di codice. I cicli sono: while, for, range

--While--
Reitera un blocco di codice finchè una condizione è vera
es while:
while 1>0: #condizione sempre vera
    print("Ciao)
Il codice stamperà "ciao" all'infinito.

Il ciclo while viene utilizzato quanto non si conosce il numero necessario di reiterazioni

--FOR--
Al contrario di while, for viene utilizzato quando si conosce il numero di ripetizioni di una parte di codice necessarie. Viene utilizzata su una sequenza di elementi come liste, tuple o oggetti
es for:
lista = [1,2,3]
for n in lista:
    print("Ciao")
Per quanti sono i valori all'interno della lista, verrà replicato il ciclo

--RANGE--
è una funzione incorporata in Python che restituisce una sequenza di numeri interi che possono essere utilizzati in cicli for o in altre situazioni in cui è necessario iterare su un insieme di valori.
      """)


#
#
#
#
