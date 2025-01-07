#output list
import os,time
radekoutputstart = ["⬜"]

#nejaky values (beztak jsou tady nejaky zbytecne ale nechce se mi to opravovat)
values = []
output = {}
radkycisla = []
player1= []
player2= []
err = 0
radekvalue = 0
winvalue = 5
key= None
player =0
round = 0
vyhra = 0
remiza = 0

#values na kombinace
svisle = {}
horizontal = {}
diagonal = {}
win = 0


#funkce zadani zacatecnich values
def sizeinput():
    global radekvalue,winvalue

    print("zadejte grid tabulky např.5,10... (5 = 5x5) maximum je 30, minimum 3")
    radekvalue = int(input(">"))
    print("zadej kolik je potreba policek pro vyhru( cislo <3 = automaticky 3) maximalne je pocet radku/sloupcu")
    winvalue = int(input(">"))
    #nejakej error handling
    if winvalue <3:
        winvalue =3
        print(winvalue)
    
    if winvalue > radekvalue:
        print("spatne cislo")
        sizeinput()

    if radekvalue <3 or radekvalue >30:
        print("spatne cislo")
        sizeinput()
    else:
        #vytvoreni tabulky   
        for i in range(1, radekvalue+1):
            if i <10:
                output[f"{i}. řádek"] = ['⬜'] *radekvalue
            else:
                output[f"{i}.řádek"] = ['⬜'] *radekvalue
            radkycisla.append(i)
    

    #generator kombinaci na danou tabulku
    diagonallist = []
    count = 0
    global svislelist
    svislelist = []
    templist = []

    #svisle kombinace
    for i in range(1,radekvalue+1):
       svislelist.append(i)
       svislelist.append(i+radekvalue)     
       for j in range(1,radekvalue-1):
           svislelistlen = len(svislelist)
           lastnumlist = svislelist[svislelistlen-1]
           svislelist.append(lastnumlist+radekvalue)
    #zarazeni moznosti do dictionary {}
    for j in range(1,radekvalue+1):
       templist = []
       for i in range(radekvalue):
           templist.append(svislelist.pop(0))
           svisle[f"{j}.sloupec"] = templist
    
    #horizont kombinace
    for g in range(1,radekvalue*radekvalue, radekvalue):
       count +=1
       horizontallist =[]
       horizontallist.append(g)
       for j in range(1,radekvalue):
           horizontallist.append(g+j)
       horizontal[f"{count}.radek"] =horizontallist 
       horizontallist =[]

    # diagonal zleva kombinace
    count = 0
    prvninum = 1
    diagonallist.append(prvninum)
    for g in range(radekvalue+1,(radekvalue*radekvalue), radekvalue):
        count+=1
        diagonallist.append((prvninum*count)+g)
    diagonal["zleva"] = diagonallist
    
    #diagonal zprava kombinace
    diagonallist = []
    count = 0
    diagonallist.append(radekvalue)
    for g in range(radekvalue*2,(radekvalue*radekvalue)+1, radekvalue):
        count+=1
        diagonallist.append(g-count)
    diagonal["zprava"] = diagonallist

#print tabulky pomoci dictionary
def tabulka():
    os.system("cls")
    for k,v in output.items():
        print(f"{k}:{v}")
    print("           ", end="")
    if radekvalue <11:
        for g in range(1, radekvalue +1):
            print(f"{g}.",end="    ")
    else:
        for g in range(1, 12):
            print(f"{g}.",end="    ")
        for g in range(12, radekvalue+1):
            print(f"{g}.",end="   ")
    print("\n")

    
def inputchoice():
    global radek,sloupec,round,continueinput,err
    radek = 0
    sloupec = 0
    err = 0
    continueinput = 0
    
    #moznost drivejsi remizy
    if round > radekvalue:
        print("chcete pokracovat?")
        print("1.ano")
        print("2.vzdat se (remiza)")
        continueinput = int(input(">"))
        match continueinput:
             case 1:
                pass
             case 2:
                  tiescreen()
             case _:
                print("spatnecislo")
                err=1

    print(f"{round}. kolo {player}. hráč: napiš číslo řádku 1-{radekvalue}")
    radek = int(input(">"))
    if radek not in radkycisla:
        print(f"pouze cisla 1-{radekvalue}")
        inputchoice()
    else: 
        print(f"{round}. kolo {player}. hráč: napiš číslo sloupce 1-{radekvalue}")
        sloupec = int(input(">"))
        if sloupec not in radkycisla:
            print(f"pouze cisla 1-{radekvalue}")
            inputchoice()

#zaradi input do dictionary a do tabulky
def evaluateinput():
    global key,keylist,player,radek,sloupec,err,num
    num = 0
    err = 0

    #projede to dictionary a najde spravnej radek do kteryho da emoji a do player inputu cislo
    if radek <10:
        key = f"{radek}. řádek"
    else:
        key = f"{radek}.řádek"
    keylist = output.get(key)

    num = ((radek-1) * radekvalue) + sloupec
    if num in player1 or num in player2:
        print("Místo je uz obsazene\n")
        err = 1
    else:
        if player ==1:
            keylist[sloupec-1]  ="❌"
            player1.append(num)
        if player ==2:
            keylist[sloupec-1]  ="🔵"
            player2.append(num)

#loopu ktery projizdi mozny kombinace s player listama ve kterych je input
def checkcombinations():
    global win
    if round > 2:
        win = 0
        for i in range(1,radekvalue+1):
            if win ==1:
                break
            keyhorizontal = f"{i}.radek"
            keysvisle = f"{i}.sloupec"
            keydiagonal1 = "zleva"
            keydiagonal2 = "zprava"
            #horizontal
            cislakeys = horizontal.get(keyhorizontal)
            count = 0
            for j in cislakeys:
                for g in player1:
                    if g ==j:
                        count +=1
            if count == winvalue:
                if player ==1:
                    win = 1
                if player ==2:
                    win = 2
                break
            #svisle 
            cislakeys = svisle.get(keysvisle)
            count = 0
            for j in cislakeys:
                for g in player1:
                    if g ==j:
                        count +=1
            if count == winvalue:
                if player ==1:
                    win = 1
                if player ==2:
                    win = 2
                break
            #diagonal 1
            cislakeys = diagonal.get(keydiagonal1)
            count = 0
            for j in cislakeys:
                for g in player1:
                    if g ==j:
                        count +=1
            if count == winvalue:
                if player ==1:
                    win = 1
                if player ==2:
                    win = 2
                break
            #diagonal 2
            cislakeys = diagonal.get(keydiagonal2)
            count = 0
            for j in cislakeys:
                for g in player1:
                    if g ==j:
                        count +=1
            if count == winvalue:
                if player ==1:
                    win = 1
                if player ==2:
                    win = 2
                break

def winscreen():
    global vyhra
    tabulka()
    print(f"Vyhrál {player}. hráč 🎉")
    vyhra = 1
    print('restarting...')
    time.sleep(3)

def tiescreen():
    global remiza
    tabulka()
    print(f"REMIZA")
    remiza = 1
    print('restarting...')
    time.sleep(3)

#trochu error handling ale trochu to blbe funguje a nechce se mi to fixovat
def errhandling():
    global err,player,round
    err = 1
    while err ==1 and vyhra != 1 :
        inputchoice()
        evaluateinput()

#prvni kolo hry
def StartGame():
        global player,round
        sizeinput()
        # print(svisle,horizontal,diagonal)
        player =1
        round =1
        tabulka()
        errhandling()
        tabulka()
        player =2
        errhandling()
        tabulka()

while True:
#prvnikolo
    print("TICTACTOE")
    print("Starting game..")
    time.sleep(3)
    StartGame()

#nasledujici kola
    while vyhra != 1 or remiza != 1 :
        player =1
        round +=1 
        tabulka()
        errhandling()

        checkcombinations()
        if win !=0:
            print(F'VYHRA {player}. hráč 🎉🎉🎉🎉🎉🎉🎉')
            break
        tabulka()
        player =2
        errhandling()
        checkcombinations()
        tabulka()
    print("Restarting game..")
    time.sleep(3)
