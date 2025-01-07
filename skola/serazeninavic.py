pocetcisel = int(input(">počet čísel:"))

nejvetsicislo = 0
druhynejvetsicislo = 0
seznamcisel = []
vyskyt = []


#najde nejvetsi cislo, kazde cislo hodi do seznamu
for i in range(pocetcisel):
    cislo = int(input(f">vlož {i+1}.číslo:"))
    if cislo >= nejvetsicislo:
        nejvetsicislo = cislo
    seznamcisel.append(cislo)

#projede celej seznam a vymaze nejvetsi cisla
while nejvetsicislo in seznamcisel:
    seznamcisel.remove(nejvetsicislo)

#projede seznam a zjisti jaky je druhy nejv.cislo
for i in seznamcisel:
    if i >= druhynejvetsicislo:
        druhynejvetsicislo = i

#spocitani kolikrat tam druhy nej. cislo je
for i in seznamcisel:
    if i == druhynejvetsicislo:
        vyskyt.append(i)

print(f">nejvetsi:{nejvetsicislo}")
print(f">druhy nejvetsi:{druhynejvetsicislo}")
print(f"vyskyt druheho nejvetsiho cisla:{len(vyskyt)}")