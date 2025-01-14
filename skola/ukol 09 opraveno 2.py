listcisel = [3,1,56,7,5,3,2]

# smaze z seznamu stejna cisla = [3,1,2,3] -> [3,1,2]
for i in listcisel:
    filtr = 0
    for g in listcisel:
        if i == g:
            filtr +=1
            if filtr > 1:
                listcisel.remove(i)                

#loop projizdeni cisel
for i in range(0,len(listcisel)):
    nejvetsi = 0
    for j in range(i,len(listcisel)):
        cislo = listcisel[j]
        if cislo > nejvetsi:
            nejvetsi = cislo
    listcisel.remove(nejvetsi)
    listcisel.insert(i,nejvetsi)
print(f"Seřazeno: {listcisel}")




    
