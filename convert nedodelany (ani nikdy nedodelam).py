import os 
nasobek = 0
jednotka = 0
cislo = 0

def clear():
    os.system("cls")

def jednotkydelka():
    print("1. mm")
    print("2. cm")
    print("3. dm")
    print("4. m")
    print("5. km")

def vypocet(cislo, nasobek,jednotka):
    vysledek = cislo * nasobek
    formatted_km = f"{vysledek:.1e}"
    print (formatted_km,jednotka)

clear()
print("---convert---")
print("1. delka")
print("2. obsah")
print("3. objem")
print("4. hmotnost")
print("5. rychlost")
print("6. cas")
print("7. teplota")
print("8. mena")
volbastart = int(input(">"))
match volbastart:
    case 1:
        clear()
        print("z jaké jednotky?")
        jednotkydelka()  
        volbadelkaz = int(input(">"))
        match volbadelkaz:
            case 1:
                clear()
                print("na jakou jednotku?")
                jednotkydelka()
                volbadelkana = int(input(">"))
                match volbadelkana:
                    case 1:
                        clear()
                        print("vlož číslo")
                        cislo = int(input(">"))
                        nasobek = 1
                        jednotka = "mm"
                        vypocet(cislo,nasobek,jednotka)
                    case 2:
                        clear()
                        print("vlož číslo")
                        cislo = int(input(">"))
                        nasobek = 0.1
                        jednotka = "cm"
                        vypocet(cislo,nasobek,jednotka)
                    case 3:
                        clear()
                        print("vlož číslo")
                        cislo = int(input(">"))
                        nasobek = 0.01
                        jednotka = "dm"
                        vypocet(cislo,nasobek,jednotka)
                    case 4:
                        clear()
                        print("vlož číslo")
                        cislo = int(input(">"))
                        nasobek = 0.001
                        jednotka = "m"
                        vypocet(cislo,nasobek,jednotka)
                    case 5:
                        clear()
                        print("vlož číslo")
                        cislo = int(input(">"))
                        nasobek = 0.000001
                        jednotka = "km"
                        vypocet(cislo,nasobek,jednotka)

    
    
    case 2:         
        print(True)
    case 3:
        print(True)
    case 4:
        print(True)
    case 5:
        print(True)
    case 6:
        print(True)
    case 7:
        print(True)
    case 8:
        print(True)

# delka, obsah, objem
#hmotnost
#km/h na m/s
#km na mi
#cas
# celsius na fahrnheit, kelvin
#mena