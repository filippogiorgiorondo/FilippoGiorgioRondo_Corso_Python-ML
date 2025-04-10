#l'input stringa viene reso tutto minuscolo e salvato in una variabile
nomeInserito =input("inserisci il tuo nome: ").lower()

#verifica che l'input sia uguale a "mirko" per superare il primo livello
if nomeInserito == "mirko":
    print("complimenti hai superato il primo livello\nPreparati al prossimo!..")
    
    #si prepara a ricevere un input da considerare come numero intero
    numeroInserito = int(input("Inserisci un numero da 1 a 10: "))
    
    #se l'input è uguale a '1', supera il secondo livello
    if numeroInserito == 1:
        print("Complimenti hai superato il secondo livello\nPreparati al prossimo!..")
        
        #l'input stringa viene reso tutto minuscolo e salvato in una variabile
        animalePreferito = input("Indovina il mio animale preferito..Inizia con la C: ").lower()
        
        #se l'input inserito è uguale a 'cane', il livello viene superato
        if animalePreferito == "cane":
            print("Gioco completato")
