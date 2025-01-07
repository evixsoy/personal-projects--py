nejvetsicislo = 0
nejmensicislo = 0
opakovani = 1

while opakovani == 1:
    cislo= int(input("vlož číslo:"))
    if cislo == 0:
        opakovani = 0
    else:
        if cislo < nejmensicislo or nejmensicislo == 0:
            nejmensicislo = cislo
        elif cislo > nejvetsicislo:
            nejvetsicislo = cislo

print(f">nejvetsi:{nejvetsicislo} ,nejmensi:{nejmensicislo}")