def zeigeMenu():
    
    print("===============") 
    print("Getränkeautomat")
    print("===============")
    print("Bitte Ihr Getränk auswählen")
    print("1) Kaffee 3,50 €")
    print("2) Kakao 1,50 €")
    print("3) Tee 1,00 €")
    print("x) Automat beenden")

def getränkeWahl():
    try: 
        auswahl = input("Ihr Wahl: ")
        
        preise = {"1": 350,"2": 150,"3": 100}
    
        getränkeNamen = {"1": "Kaffee","2": "Kakao","3": "Tee"}
      
        getränk = getränkeNamen[auswahl]
        kosten = preise[auswahl]
    except:
        return getränkeWahl
    
    match auswahl:
        case "1":
            print(f"Sie haben {getränk} gewählt")
            print("-------------------------------")
            print(f"Offene Kosten: {kosten} cent")
            print("-------------------------------")
            
            kosten = geldBezahlen(kosten)
            if kosten <= 0:
                print("-------------------------------")
                print("Rest ist ", "{kosten}-{geldBezahlen}", "cent")
                print("-------------------------------")
                print("Sie haben passend gezahlt")
                print("Vielen Dank! Ihr Getränk wird vorbereitet.")
            else:
                print(f"Offene Kosten nach Zahlung: {kosten} - {geldBezahlen} ")
                

        case "2":
            print(f"Sie haben {getränk} gewählt")
            print("-------------------------------")
            print(f"Rest ist: {kosten} cent")
            print("-------------------------------")

            kosten = geldBezahlen(kosten)
            if kosten <= 0:
                print("Vielen Dank! Ihr Getränk wird vorbereitet.")
            else:
                print(f"Offene Kosten nach Zahlung: {kosten} - {geldBezahlen} ")

        case "3":
            print(f"Sie haben {getränk} gewählt")
            print("-------------------------------")
            print(f"Offene Kosten: {kosten} cent")
            print("-------------------------------")

            kosten = geldBezahlen(kosten)
            if kosten <= 0:
                print("Vielen Dank! Ihr Getränk wird vorbereitet.")
            else:
                print(f"Offene Kosten nach Zahlung: {kosten} - {geldBezahlen} cent")
        case "x":
            print("Automat wird beendet.")
        case _:
            print("Ungültige Auswahl, bitte erneut versuchen.")

def geldBezahlen(kosten):
    münzen = {"1": 5,"2": 10,"3": 20,"4": 50,"5": 100,"6": 200}
    
    while kosten > 0:
        print("Bitte Münze eingeben:")
        print("1) 5 cent")
        print("2) 10 cent")
        print("3) 20 cent")
        print("4) 50 cent")
        print("5) 1 €")
        print("6) 2 €")
        
        wahl = input("Ihre Wahl: ")
        kosten -= münzen[wahl]
        
        match wahl:
            
            case "1":                
                print(f"Sie haben {münzen[wahl]} cent eingeworfen.")
            case "2":
                print(f"Sie haben {münzen[wahl]} cent eingeworfen.")
            case "3":
                print(f"Sie haben {münzen[wahl]} cent eingeworfen.")
            case "4":
                print(f"Sie haben {münzen[wahl]} cent eingeworfen.")
            case "5":
                print(f"Sie haben {münzen[wahl]} cent eingeworfen.")
            case "6":
                print(f"Sie haben {münzen[wahl]} cent eingeworfen.")
            case _:
                print("Ungültige Münze, bitte erneut versuchen.")
        
        print("-------------------------------")
        print(f"Offene kosten {kosten} cent")
        print("-------------------------------")

    
    else :
        return kosten
  

weitereGetraenke = True
while weitereGetraenke:
    zeigeMenu()
    getränkeWahl()
else:
    print("Programmende")
