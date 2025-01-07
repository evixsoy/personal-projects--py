listcisel = []
sort = []
inputcisla = None
print("pis cisla(0 se ukonci program)")

while True:
    inputcisla = int(input(">"))
    if inputcisla ==0:
        break
    listcisel.append(inputcisla)

cisla = len(listcisel)
nejmensi = listcisel[0]

for x in range(1,cisla+1):
    for i in listcisel: 
        nejmensi = listcisel[0]
        for j in listcisel: 
            if j<i or j==i:
                if nejmensi > j:
                    nejmensi = j


    sort.append(nejmensi)
    listcisel.remove(nejmensi)

print(sort)


#algorithm 2

cisla = [3,45,53,2,445,5,6]

for i in range(len(cisla)):
    nejvetsi = cisla[i]  
    index_nejvetsi = i   
    
    for j in range(i + 1, len(cisla)): 
        if cisla[j] > nejvetsi:
            nejvetsi = cisla[j]
            index_nejvetsi = j


    cisla.pop(index_nejvetsi)
    cisla.insert(i, nejvetsi)


print(cisla)