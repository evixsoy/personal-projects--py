strop = int(input("Strop:"))
cifcislo = int(input("Ciferne cislo:"))
cifvypocet = 0
pocet = 0

#cisla napr 1->99, prevede na string
for i in range(1,strop):
    istr= str(i)
    
    # rozdeli cisla např. 150 na 1,5,0, vypocita je
    for j in istr:
        cifvypocet = int(cifvypocet)+int(j)
    
    if cifvypocet == cifcislo:
        print(i)
        pocet =1

    cifvypocet = 0

if pocet != 1:
    print("nenalezeno zadne cislo")



