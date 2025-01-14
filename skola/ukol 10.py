zpravainput = input("Zadej zpravu:").lower()
klic = input("Zadej klic:").lower()
abeceda = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listpozic = []
pozice = 0
zprava = ""

#filtr mezer
for i in zpravainput:
    if i != " ":
        zprava += i
        

#zjisteni pozit pismen v klici
for i in klic:    
    for g in abeceda:        
        pozice += 1        
        if i ==g:            
            listpozic.append(pozice)            
            pozice = 0            
            break

asciizprava = []
lenpozic = len(listpozic)
cislo = -1
output = ""
hodnotysifer = []

#prevod zpravy do ascii
for i in zprava:
    asciizprava.append(ord(i))

#zcitati a output
for i in asciizprava:
    cislo += 1    
    if cislo == lenpozic:        
        cislo = 0    
    hodnotasifra = i + listpozic[cislo]    
    if hodnotasifra > 122:
        hodnotasifra = hodnotasifra -26
    hodnotysifer.append(hodnotasifra)   
    # print(hodnotasifra)    
    output += chr(hodnotasifra)
# print(asciizprava)
# print(listpozic)
# print(hodnotysifer)
print(f"output: {output}")