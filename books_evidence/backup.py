#WIP

def menu():
    print("1. Zobrazit seznam knih \n2. Vyhledat knihu \n3. Přidat novou knihu \n4. Upravit údaje knihy \n5. Odstranit knihu \n6. Zobrazit statistiky \n7. Ukončit program")
    valueinput = min(7, max(1, int(input(">"))))
    return valueinput

class UzivatelskaChyba(Exception):
    pass
def seznamknih():
    ids =[]
    autor = []
    rok = []
    zanr = []
    pocetkusu = []
    kniha = []
    with open('books.txt',encoding='UTF-8') as fileread:
        contents = fileread.read().splitlines()
    for i in contents:
        hodnoty = i.split(";")
        ids.append(hodnoty[0])
        kniha.append(hodnoty[1].lower())
        autor.append(hodnoty[2].lower())
        rok.append(hodnoty[3])
        zanr.append(hodnoty[4].lower())
        pocetkusu.append(hodnoty[5])
        # for i in range(len(ids)):
        # print(f"ids: {ids[i]} | nazev knihy: {kniha[i]} | autor: {autor[i]} | rok vydani: {rok[i]} | zanr: {zanr[i]} | pocet kusu: {pocetkusu[i]}")
    return ids,kniha,autor,rok,zanr,pocetkusu

def capitalize_seznam(string):
    newstring = f"{string[0]}"
    for i in range(len(string)-1):
        prvnisymbol = string[i]
        druhysymbol = string[i+1]
        #pridat vic moznosti kdy muze byt velke pismeno
        if prvnisymbol == " " and druhysymbol.isalpha() or prvnisymbol == "." and druhysymbol.isalpha() :
            druhysymbol = druhysymbol.capitalize()
        newstring += druhysymbol
    return newstring

def zobrazitseznam(ids,kniha,autor,rok,zanr,pocetkusu):
    for i in range(len(ids)):
        print(capitalize_seznam(string=f"ids: {ids[i]} | nazev knihy: {kniha[i].capitalize()} | autor: {autor[i].capitalize()} | rok vydani: {rok[i]} | zanr: {zanr[i].capitalize()} | pocet kusu: {pocetkusu[i]}"))

def vyhledatknihu(ids,kniha,autor,rok,zanr,pocetkusu):
    print("1. podle ID \n2. názvu \n3. podle autora \n4. podle roku vydani \n5. podle zanru \n6. poctu kusu ")
    try:
        valueinput = min(6, max(1, int(input(">"))))
        category = None
        not_found = 0
        match valueinput:
            case 1:
                print("zadejte id:")
                valueinput = int(input(">"))
                try:
                    print(f"ids: {ids[valueinput-1]} | nazev knihy: {kniha[valueinput-1]} | autor: {autor[valueinput-1]} | rok vydani: {rok[valueinput-1]} | zanr: {zanr[valueinput-1]} | pocet kusu: {pocetkusu[valueinput-1]}")
                except IndexError:
                    print("spatne cislo")
                    raise UzivatelskaChyba
            case 2:
                temp_value = str(input("Napiš název knihy: ")).lower()
                category = kniha
            case 3:
                temp_value = str(input("Napiš název autora: ")).lower()
                category = autor
            case 4:
                temp_value = input("Napiš rok vydani: ")
                category = rok
            case 5:
                temp_value = str(input("Napiš žánr: ")).lower()
                category = zanr
            case 6:
                temp_value = input("Počet kusů: ")
                category = pocetkusu
            case _:
                raise UzivatelskaChyba
        krok = 0
        for i in category:
            if i == temp_value:
                string = capitalize_seznam(f"ids: {ids[krok]} | nazev knihy: {kniha[krok]} | autor: {autor[krok]} | rok vydani: {rok[krok]} | zanr: {zanr[krok]} | pocet kusu: {pocetkusu[krok]}") 
            else:
                not_found += 1
            krok += 1
        if not_found == len(category):
            print("Polozka nenalezena")
            #TODO vratit na menu
                
    except UzivatelskaChyba:
        print("WIP")
        #TODO vratit na input, asi udelat nejakej chod programu
    
    return string

def pridat_polozku(ids):
    #napsani do txt
    nove_id = len(ids)+1
    print("Název Knihy:")
    nove_kniha = input(">")
    print("Název Autora:")
    novy_autor = input(">")
    print("Rok vydání:")
    novy_rok = input(">")
    print("Žánr:")
    novy_zanr = input(">")
    print("Počet kusů:")
    nove_pocet = input(">")
    print(f"Takhle v pořádku?: {capitalize_seznam(string = f"ids: {nove_id} | nazev knihy: {nove_kniha} | autor: {novy_autor} | rok vydani: {novy_rok} | zanr: {novy_zanr} | pocet kusu: {nove_pocet}")}")
    print(f"1.ANO\n2.NE")
    volba = int(input(">"))
    match volba:
        case 1:
            print(True)
            with open('books.txt',"a", encoding='UTF-8') as stringappend:
                stringappend.write(f"\n{nove_id};{nove_kniha};{novy_autor};{novy_rok};{novy_zanr};{nove_pocet}")
            
        case 2:
            #zpet na zacatek, asi raise uzivatelska chyba ig 
            pass
        case _:
            #err handling
            pass
            
def upravit_polozku():
    pass
    #vyhledatknihu(), vsechny knihy od nalezene knihy po konec seznamu (a smaze je) => budou nacteny v listu aji s uz zmenenym seznamem => na konci programu se cely list hodi do txt
            
ids,kniha,autor,rok,zanr,pocetkusu= seznamknih()
zobrazitseznam(ids,kniha,autor,rok,zanr,pocetkusu)
string = vyhledatknihu(ids,kniha,autor,rok,zanr,pocetkusu)

# pridat_polozku(ids)

def chod_programu():
    valueinput = 1
    while valueinput != 0:
        valueinput = menu()
        match valueinput:
            case 1:
                zobrazitseznam()
            case 2:
                vyhledatknihu()




