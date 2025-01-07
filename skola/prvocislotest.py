while True:
    cislo = int(input(">"))
    filtr = 0
    
    if cislo !=1:
        for i in range(2,cislo):
            mezipocet = cislo/i
            if mezipocet.is_integer():
                filtr = 1

        if filtr == 1 :
            print("neni prvocislo")
        else:
            print("je prvocislo")
    else:
        print("je prvocislo")
    
        
