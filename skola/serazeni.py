pocetcisel = int(input(">počet čísel:"))

nejvetsicislo = 0
nejmensicislo = 0
seznamcisel = []
vyskyt = []


for i in range(pocetcisel):
    cislo = int(input(f">vlož {i+1}.číslo:"))
    if cislo < nejmensicislo or nejmensicislo == 0:
        nejmensicislo = cislo
    elif cislo > nejvetsicislo:
        nejvetsicislo = cislo
    seznamcisel.append(cislo)

for i in seznamcisel:
    if i == nejvetsicislo:
        vyskyt.append(i)

print(f">nejvetsi:{nejvetsicislo} ,nejmensi:{nejmensicislo}")
print(f">vyskyt nejvetsiho cisla:{len(vyskyt)}krát")