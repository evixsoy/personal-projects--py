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
        kniha.append(hodnoty[1])
        autor.append(hodnoty[2])
        rok.append(hodnoty[3])
        zanr.append(hodnoty[4])
        pocetkusu.append(hodnoty[5])
        # for i in range(len(ids)):
        # print(f"ids: {ids[i]} | nazev knihy: {kniha[i]} | autor: {autor[i]} | rok vydani: {rok[i]} | zanr: {zanr[i]} | pocet kusu: {pocetkusu[i]}")
    return ids,kniha,autor,rok,zanr,pocetkusu

def vyhledatknihu(ids,kniha,autor,rok,zanr,pocetkusu):
    print("1. podle ID \n2. názvu \n3. podle autora \n4. podle roku vydani \n5. podle zanru \n6. poctu kusu ")
    try:
        valueinput = min(6, max(1, int(input(">"))))
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
                print("zadejte název:")
                valueinput = input(">")  
    except UzivatelskaChyba:
        print("WIP")
        #TODO vratit na input
            
ids,kniha,autor,rok,zanr,pocetkusu= seznamknih()
vyhledatknihu(ids,kniha,autor,rok,zanr,pocetkusu)


# vyhledatknihu()


