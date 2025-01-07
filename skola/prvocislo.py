while True:
    cislo = int(input(">"))
    pocet = 0
    for i in range(2,cislo):
       #vydělí input číslem od 2 až do inputu a převede do stringu
       mezipocet = str(cislo/i)
       #číslo v stringu zkontroluje jestli je číslo celé
       if mezipocet.endswith("0"):
           pocet = +1

    if pocet >=1 or cislo == 1:
           print("neni prvocislo")
    else:
           print("je prvocislo")
