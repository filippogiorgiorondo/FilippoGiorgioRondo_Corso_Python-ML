whatdo = input("Benvenuto nel programma 'pari o dispari'. Digitare 1 se interessato ad un numero intero, digitare 2 se interessato ad una stringa")
match whatdo:
  case "1":
    numero = int(input("Inserire il numero da verificare"))
    if numero % 2 == 0:
      print("Il numero inserito è pari")
    else:
      print("Il numero inserito è dispari")

  case "2":
    stringa = input("Inserisci qui la tua stringa (non accettati gli spazi)")
