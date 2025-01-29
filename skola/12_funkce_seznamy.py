def novyseznam():
    cislaseznamu = 1
    seznam = []
    print("Napiš čísla do seznamu (0 se ukonci)")
    while cislaseznamu != 0:
        cislaseznamu = int(input(">"))
        seznam.append(cislaseznamu)
    seznam.remove(0)
    return seznam

def menu():
    print("Zvolte moznost:\n 1. Zobrazit seznam \n 2. Seřadit seznam podle nejvetsiho \n 3. Zobrazit prvocisla \n4. Změnit seznam")
    vyber = int(input(">"))
    return vyber

def zobrazitseznam(seznam):
    print(seznam)

def seraditseznam(seznam):
    for i in range(0, len(seznam)):
        nejvetsi = 0
        for j in range(i, len(seznam)):
            cislo = seznam[j]
            if cislo > nejvetsi:
                nejvetsi = cislo
        seznam.remove(nejvetsi)
        seznam.insert(i, nejvetsi)
    return seznam

def seznam_prvocisel(seznam):
    #zapisovani do seznamu
    listprvocisel = []
    for i in seznam:
        check = is_prvocislo(i)
        if check != None:
            listprvocisel.append(check)
    return listprvocisel

def is_prvocislo(cislo):
    pocet = 0
    for i in range(2, cislo):
        mezipocet = str(cislo / i)
        if mezipocet.endswith("0"):
            pocet = +1
    if pocet >= 1 or cislo == 1:
        pass
    else:
        return cislo

def chovani_programu():
    vyber = 1
    seznam = novyseznam()
    while vyber != 0:
        vyber = menu()
        match vyber:
            case 1:
                zobrazitseznam(seznam)
            case 2:
                print(seraditseznam(seznam))
            case 3:
                print(seznam_prvocisel(seznam))
            case 4:
                seznam = novyseznam()
            case _ :
                print("spatne cislo")
chovani_programu()


