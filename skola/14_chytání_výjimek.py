def inputseznam():
    cislaseznamu = 1
    seznam = []
    print("Napiš čísla do seznamu (0 se ukonci)")
    while cislaseznamu != 0:
        try:
            cislaseznamu = int(input(">"))
        except ValueError:
            print("Špatné číslo")
        else:
            seznam.append(cislaseznamu)
    seznam.remove(0)
    return seznam

listcisel = inputseznam()
print(f"Váš seznam:{listcisel}")
cislo = 0
for i in listcisel:
    cislo += i
try:
    print(f"Průměrná hodnota je: {cislo/len(listcisel):.1f}")
except ZeroDivisionError:
    print("Nelze dělit nulou !")




