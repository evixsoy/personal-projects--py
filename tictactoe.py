#cca roadmap jak to funguje:
#https://miro.com/app/board/uXjVL3QGRs0=/?share_link_id=144240377145

import os,time

#output list
prvnir = ["⬜","⬜","⬜"]
druhyr = ["⬜","⬜","⬜"]
tretir = ["⬜","⬜","⬜"]
combinations = [1, 2, 3], [4, 5, 6], [7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]

#player promenne(mozna tady je neco zbytecne jsem linej)
playerone=[]
playertwo=[]
radek = 0
sloupec = None
cislo = 0
round = 1
player = 0
err = 0
vyhra = 0
pocitadlo = 0

def tabulka():
    global pocitadlo
    os.system("cls")
    print("/----------------\\")
    print(f"|1.ř:  {prvnir[0]} | {prvnir[1]} | {prvnir[2]} |")
    print(f"|2.ř:  {druhyr[0]} | {druhyr[1]} | {druhyr[2]} |")
    print(f"|3.ř:  {tretir[0]} | {tretir[1]} | {tretir[2]} |")
    print("\\----------------/")
    if pocitadlo > 8 and vyhra == 0:  # Kontrola na začátku
        pocitadlo= 100 # = remiza

#funkce na vsechy inputy i s error handling
def inputtab():
    global radek,sloupec,cislo,pocitadlo
    cislo = 0
    radek = 0
    sloupec = 0
    if pocitadlo > 8 and vyhra == 0:  # Kontrola na začátku
        pass
    else:       
        print("napiš číslo řádku 1-3:")
        radek = int(input(">"))
    
        if radek not in [1, 2, 3]:
            print("pouze cisla 1-3")
            print(radek)
            inputtab()
    
        else: 
            print("napiš číslo sloupce 1-3:")
            sloupec = int(input(">"))
    
            if sloupec not in [1,2,3]:
                print("pouze cisla 1-3")
                inputtab()
            else:
                pass

#cislo policka se priradi k spravnymu cislu
def listappend():
    global radek, sloupec,cislo,outputrad
    if radek == 1:
        outputrad = prvnir
        if sloupec ==1:
            cislo  = 1
        if sloupec ==2:
            cislo  = 2
        if sloupec ==3:
            cislo  = 3
    if radek == 2:
        outputrad = druhyr
        if sloupec ==1:
            cislo  = 4
        if sloupec ==2:
            cislo  = 5
        if sloupec ==3:
            cislo  = 6
    if radek == 3:
        outputrad = tretir
        if sloupec ==1:
            cislo  = 7
        if sloupec ==2:
            cislo  = 8
        if sloupec ==3:
            cislo  = 9

#check jestli dane cislo uz v jednom z listu neni(aby se nemohli menit uz zabrane policka) a hodi cislo do player listu
def playervyhodnoceni():
    global err,pocitadlo
    err = 0
    if player ==1:
        if cislo in playertwo:
            print("ERROR")
            err = 1
            return
        if cislo in playerone:
            print("ERROR")
            err = 1
            return
        playerone.append(cislo)
        pocitadlo += 1
        if err ==0:
            outputrad.insert(sloupec, "❌")
            outputrad.pop(sloupec-1)
            
    else:
        if cislo in playertwo:
            print("ERROR")
            err = 1
            return
        if cislo in playerone:
            print("ERROR")
            err = 1
            return
        playertwo.append(cislo)
        pocitadlo += 1
        if err ==0:           
            outputrad.insert(sloupec,"0️⃣ ")
            outputrad.pop(sloupec-1)
            

#projede to vsechny mozne kombinace vyhry(snad) a da check s player listem jestli uz nevyhral
def checkcombinations():
    global vyhra
    if round>2:
        if player ==2:
        #object combinatins
            for i in combinations:
                nalezeni = 0
                #items in objects
                for j in i:
                    for z in playertwo:
                        if z == j:
                            nalezeni +=1
                if nalezeni ==3:
                    vyhra = 2
        else:
            for i in combinations:
                nalezeni = 0
                #items in objects
                for j in i:
                    for z in playerone:
                        if z == j:
                            nalezeni +=1
                if nalezeni ==3:
                    vyhra = 1
#kdyz uzivatel zadana policko ktere uz bylo zabrane tak aby ho to hodilo zpet na input
def errhry():
    global err,pocitadlo
    err = 1
    while err ==1 :
        inputtab()
        listappend()
        playervyhodnoceni()

#funkce aby hra sla postupne podle funkci, nejake vyhodnocovani vyhry
def playgame():
    global player,round
    player = 1
    tabulka()
    print(f"kolo {round}. Hráč 1:")
    errhry()
    checkcombinations()
    round +=1
    if vyhra ==1 :
        pass
    else:
        player = 2
        tabulka()
        print(f"kolo {round-1}. Hráč 2:")
        errhry()
        checkcombinations()
        tabulka()
#resetuje data do puvod stavu(slo by udelat chytrejc)
def WipeData():
    global prvnir,druhyr,tretir,combinations,player,playerone,playertwo,radek,sloupec,cislo,round,err,vyhra,pocitadlo
    prvnir = ["⬜","⬜","⬜"]
    druhyr = ["⬜","⬜","⬜"]
    tretir = ["⬜","⬜","⬜"]
    combinations = [1, 2, 3], [4, 5, 6], [7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]

    #player promenne(mozna tady je neco zbytecne jsem linej)
    playerone=[]
    playertwo=[]
    radek = 0
    sloupec = None
    cislo = 0
    round = 1
    player = 0
    err = 0
    vyhra = 0
    pocitadlo = 0
    print("Nová hra")
    time.sleep(2)
def NewGame():
    while round <4:
        playgame()

    #pokracovani kdyz hrac nevyhraje v prvnich 3 tazich
    while round >= 4 and vyhra == 0:
        if pocitadlo == 100:
            print("test")  # Kontrola na začátku
            break
        playgame()

    if vyhra ==0:
        tabulka()
        print("remiza!")
    #vyhdnoceni vyhry
    if vyhra ==1 or vyhra==2:
        tabulka()
        print(f"VYHRAL {vyhra}.hráč ")
    WipeData()
    
#konecne uz start programu xd
#start kdy uzivatel jeste nemuze vyhrat(asi)
while True:
    NewGame()