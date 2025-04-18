import numpy as np

def esecuzione_programma_completo():
    # Somma e Media di Elementi
    def menu_es1_recap():
        def crea_array():
            # Crea un array di 15 numeri interi casuali tra 1 e 100
            arr = np.random.randint(1,101, size=50)

            # Stampa l'array generato
            print(f"Array generato:\n{arr}")
            return arr

        def somma_array(arr):
            # Calcola la somma di tutti gli elementi
            somma = np.sum(arr)
            print("\nSomma degli elementi:", somma)
            

        def media_array(arr):
            # Calcola la media degli elementi
            media = np.mean(arr)
            print("Media degli elementi:", media)
            
        def menu():
            print("==== BENVENUTO NELL'ESERCIZIO 1 DI RECAP ====")   
            print("Iniziamo generando un array di 15 numeri interi casuali tra 1 e 100") 
            arr = crea_array()
            while True:
                scelta = input("Tra le operazioni disponibili che puoi fare con questo array hai:\n1. Calcola somma degli elementi\n2. Calcola la media degli elementi\n3. Esci dal programma: ")
                match scelta:
                    case "1":
                        somma_array(arr)
                    case "2":
                        media_array(arr)
                    case "3":
                        print("Ritorno al menu principale")
                        break
                    case _:
                        print("Scelta non valida, riprova")
        menu()

    # Esercizio 2: Manipolazione di Array Multidimensionali
    def menu_es2_recap():

        # Estrai e stampa la seconda colonna
        def stampa_seconda_colonna(matrice):
            seconda_colonna = matrice[:, 1]
            print("\nGli elementi della seconda colonna sono:")
            print(seconda_colonna)

        # Estrai e stampa la terza riga
        def stampa_terza_riga(matrice):
            terza_riga = matrice[2, :]
            print("\nGli elementi della terza riga sono:")
            print(terza_riga)

        # Calcola e stampa la somma della diagonale principale
        def somma_diagonale_principale(matrice):
            somma = np.trace(matrice)
            print("\nSomma degli elementi della diagonale principale:")
            print(somma)

            # Menu con match-case
        def menu():
            while True:
                print("==== BENVENUTO NELL'ESERCIZIO 2 DI RECAP ====")
                matrice = np.random.randint(10, 51, size=(4, 4))
                print("Matrice con puoi giocare:")
                print(f"{matrice}\n")
                print("1. Mostra la seconda colonna")
                print("2. Mostra la terza riga")
                print("3. Somma elementi diagonale principale")
                print("4. Esci")

                scelta = input("Scegli un'opzione: ")

                match scelta:
                    case "1":
                        stampa_seconda_colonna()
                    case "2":
                        stampa_terza_riga()
                    case "3":
                        somma_diagonale_principale()
                    case "0":
                        print("Ritorno al menu principale")
                        break
                    case _:
                        print("Scelta non valida. Riprova.")
            return matrice
        menu()

    # Operazioni con Fancy Indexing
    def menu_es3_recap():
        
        # Seleziona elementi specifici con fancy indexing
        def seleziona_elementi_fancy(array):
            print("Verranno stampati gli elementi nelle seguenti posizioni:\n(0, 1)\n(1, 3)\n(2, 2)\n(3, 0)")
            righe = [0, 1, 2, 3]
            colonne = [1, 3, 2, 0]
            selezionati = array[righe, colonne]
            print("\nElementi selezionati con fancy indexing:")
            print(selezionati)

        # Mostra le righe dispari dell'array
        def stampa_righe_dispari(array):
            righe_dispari = array[1::2]
            print("\nRighe dispari dell'array:")
            print(righe_dispari)

        # Modifica gli elementi selezionati nel primo punto aggiungendo 10
        def modifica_elementi_fancy(array):
            righe = [0, 1, 2, 3]
            colonne = [1, 3, 2, 0]
            print("\nValori prima della modifica:")
            print(array[righe, colonne])
            
            array[righe, colonne] += 10
            
            print("\nValori dopo aver aggiunto 10:")
            print(array[righe, colonne])
            print("\nArray aggiornato:")
            print(array)

        # Menu
        def menu():
            while True:
                print("==== BENVENUTO NELL'ESERCIZIO 3 DI RECAP ====")
                
                # Genera e stampa l'array 4x4 all'avvio
                array = np.random.randint(10, 51, size=(4, 4))
                print("Array con cui puoi giocare:")
                print(f"{array}\n")
                print("1. Seleziona elementi specifici con fancy indexing")
                print("2. Mostra righe dispari dell'array")
                print("3. Modifica elementi selezionati (aggiungi 10)")
                print("0. Esci")

                scelta = input("Scegli un'opzione: ")

                match scelta:
                    case "1":
                        seleziona_elementi_fancy(array)
                    case "2":
                        stampa_righe_dispari(array)
                    case "3":
                        modifica_elementi_fancy(array)
                    case "0":
                        print("Ritorno al menu principale.")
                        break
                    case _:
                        print("Scelta non valida. Riprova.")

        menu()

    # Menu programma
    def menu():
        print("==== BENVENUTO NEL PROGRAMMA DEI 3 ESERCIZI DI RIEPILOGO SU NUMPY ====\n")
        while True:
            print("==== MENU PROGRAMMA GENERALE ====") 
            print("1. Primo esercizio- somma e media di elementi\n2. Secondo esercizio - Manipolazione di Array Multidimensionali\n3. Terzo esercizio - Operazioni con Fancy Indexing\n4. Esci: ")
            scelta = input("Cosa vuoi fare?\nScegli il numero corretto:")
            match scelta:
                case "1":
                    menu_es1_recap()
                case "2":
                    menu_es2_recap()
                case "3":
                    menu_es3_recap()
                case "4":
                    print("Arrivederci.")
                    break
                case _:
                    print("Numero inserito non valido. Riprova")
    
    menu()

esecuzione_programma_completo()