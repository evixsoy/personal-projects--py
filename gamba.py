import time
import random
     
#zacatek penez
bal = 500


def loadingr():
    print("spinning...")
    time.sleep(1)
    print("spinning...")
    time.sleep(1)
    print("spinning...")
    time.sleep(1)

def loadingbj():
    print("dealing cards...")
    time.sleep(1)
    print("dealing cards...")
    time.sleep(1)
    print("dealing cards...")
    time.sleep(1)

def barvyresult():
    if barvaresultpc in barvaodds:
        print(True)
    else:
        print(False)

def kartyvyhodnoceniloop():
    kartagen =random.randint(0,106)
    if kartagen <=7:
       #ace
        print("ACE! do you want 1 or 11?:")
        # global vysledkartaprvni
        vysledkartaprvni = int(input(">"))
        if vysledkartaprvni !=1 and vysledkartaprvni !=11 :
           vysledkartaprvni = 0
           print("pouze cisla 1/11")
           vysledkartaprvni = int(input(">"))
        print(vysledkartaprvni)
    elif kartagen >7 and kartagen <= 30:
       #king/queen/joker
       vysledkartaprvni =10
    elif kartagen > 30:
       #2-9 
         vysledkartaprvni = random.randint(2,9)
    return vysledkartaprvni

def kartyvyhodnocenipc():
     kartagen =random.randint(0,106)
     if kartagen <=7:
          listchoice = [1,11]
          vysledkartaprvni = random.choice(listchoice)
     elif kartagen >7 and kartagen <= 30:
        vysledkartaprvni =10
     elif kartagen > 30:
          vysledkartaprvni = random.randint(2,9)
     return vysledkartaprvni

def kartyvyhodnocenisilent():
     kartagen =random.randint(0,106)
     if kartagen <=7:
          listchoice = [1,11]
          vysledkartaprvni = random.choice(listchoice) 
     elif kartagen >7 and kartagen <= 30:
        vysledkartaprvni =10
     elif kartagen > 30:
          vysledkartaprvni = random.randint(2,9)
     return vysledkartaprvni

def logika():
     if firstcardpc + secondcardpc <= 16:
        #dve karty maji min nebo stejne jak 16
        print("dealer si bere treti kartu")
        thirdcardpc = kartyvyhodnocenisilent()
        print(firstcardpc + secondcardpc + thirdcardpc)
        global playercard
        global dealercard
        playercard = firstcardpc + secondcardpc + thirdcardpc
        print("součet karet dealera", firstcardpc + secondcardpc + thirdcardpc)
        dealercard = firstcardpc + secondcardpc + thirdcardpc
        if firstcardpc + secondcardpc + thirdcardpc >= 17:
            #tri karty maji vic nebo stejne jak 17
            playercard = firstcardplayer + secondcardplayer + thirdcardplayer
            dealercard = firstcardpc + secondcardpc + thirdcardpc
            vysledekbj()
        else:
            #tri karty maji min nebo stejne jak 16
            playercard = firstcardplayer + secondcardplayer + thirdcardplayer
            dealercard = firstcardpc + secondcardpc + thirdcardpc
            vysledekbj()
     else:
        # dve karty maji vic nebo stejne jak 17
        playercard = firstcardplayer + secondcardplayer
        dealercard = firstcardpc + secondcardpc
        vysledekbj()
        
def vysledekbj():
     if playercard < dealercard and dealercard <= 21:
          print("lose")
     elif playercard > dealercard and playercard <= 21:
          print("win")
     elif playercard == dealercard:
          print("tie")
     elif dealercard >= 21:
        print("win")
     elif playercard>= 21:
        print("lose")

          


     
volbaopak = "ano"
print("starting balance:",bal,"$")
while volbaopak== "ano":
    volbaopak = "ano"
    if bal == 0 :
        print("jsi na mizine")
        exit()
    print("1. roulette")
    print("2. blackjack")

    volbahra= int(input(">"))
    match volbahra:
    
    #ROULETTE
        case 1:
                print("sázka (maximalne", bal,"$):")
                sazkainput = int(input(">"))
                if sazkainput > bal:
                   print("nedostatek balance")
                   volbaopak = "ano"
                else:
                   balposazce = bal - sazkainput       
                    #vsazeni na pole
                   print("Na co chceš vsadit?")
                   print("1. čísla")
                   print("2.barvy")
                   print("3. 1-18 nebo 19-36")
                   volbasazka = int(input(">"))
                   match volbasazka:
                        #cisla
                       case 1:
                           cervena = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
                           cerna = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
                           zelena = [0, 00]
                           print("políčka:")
                           print("----------------------------------")
                           print("|3|6|9|12|15|18|21|24|27|30|33|36|")
                           print("|2|5|8|11|14|17|20|23|26|29|32|35|")
                           print("|1|4|7|10|13|16|19|24|25|28|31|34|")
                           print("|--------------|0|---------------|")
                           print("----------------------------------")
                           #randomness
                           sazkacislopc = random.randint(0,37)
                           # print(sazkacislopc)
                           sazkapole = int(input("cislo policka:"))
                           loadingr()
                           if sazkapole not in cervena and sazkapole not in zelena and sazkapole not in cerna:
                               print("pouze políčka 0 až 36")
                               volbaopak == "ano"
                           elif sazkapole != sazkacislopc:
                                print(f"{False},vyherni cislo:{sazkacislopc}")
                                bal = balposazce
                           elif sazkapole == sazkacislopc:
                                print(True)
                                bal = balposazce + 35*sazkainput
                           else:
                                print('napis jine cislo')
                                volbaopak == "ano"
                           print("aktualni balance:",bal, "$")
                       #barvy
                       case 2:
                           print("1.červená")
                           print("2.černá")
                           print("3.zelená")
                           volbabarva= int(input(">"))
                           if volbabarva == 1 or volbabarva == 2:
                                   barvaodds = list(range(0, 48))
                                   #print(barvaodds)
                                   loadingr()
                                   barvaresultpc = random.randint(0,100)
                                   #print(barvaresultpc)
                                   barvyresult()
                                   if barvaresultpc < 47:
                                       bal = balposazce + 2*sazkainput
                                   else: 
                                       bal = balposazce
                                   print("aktualni balance:",bal, "$")
                           elif volbabarva == 3:
                                   barvaodds = list(range(0, 6))
                                   #print(barvaodds)
                                   loadingr()
                                   barvaresultpc = random.randint(0,100)
                                   #print(barvaresultpc)
                                   barvyresult()
                                   if barvaresultpc < 5:
                                       bal = balposazce + 35*sazkainput
                                   else: 
                                       bal = balposazce
                                   print("aktualni balance:",bal, "$")
                           else:
                                   print("pouze 1-3")
                                   volbaopak == "ano"
                       #lower/higher           
                       case 3:
                           print("1. 1-18")
                           print("2. 19-36 ")
                           volbahl = int(input(">"))
                           if volbahl == 1 or volbahl == 2:
                                   barvaodds = list(range(0, 48))
                                   #print(barvaodds)
                                   loadingr()
                                   barvaresultpc = random.randint(0,100)
                                   #print(barvaresultpc)
                                   barvyresult()
                                   if barvaresultpc < 47:
                                       bal = balposazce + 2*sazkainput
                                   else: 
                                       bal = balposazce
                                   print("aktualni balance:",bal, "$")
                           else:
                                print("pouze cisla 1-2")
                       case _:
                             print("pouze cisla 1-3")
                             volbaopak == "ano"     
        
        
        #BLACKJACK                        
        case 2:
            print("sázka (maximalne", bal,"$):")
            sazkainput = int(input(">"))
            if sazkainput > bal:
               print("nedostatek balance")
               volbaopak = "ano"
            else:
               balposazce = bal - sazkainput
               
               loadingbj()
               
               print("tvoje karty:")
               firstcardplayer = kartyvyhodnoceniloop()
               secondcardplayer = kartyvyhodnoceniloop()
               thirdcardplayer = kartyvyhodnoceniloop()
               print(firstcardplayer, secondcardplayer)
               print("součet", firstcardplayer + secondcardplayer)   
               
               print("dealerovy karty:")
               firstcardpc = kartyvyhodnocenipc()
               secondcardpc = kartyvyhodnocenisilent()
               print(firstcardpc, "x")
               print("test druha karta dealer:", secondcardpc)
               if firstcardplayer + secondcardplayer >= 21:
                   print("victory")
                   bal = balposazce + (25/10)*sazkainput
                   print("aktualni balance:",bal, "$")
               elif firstcardpc + secondcardpc >= 21:
                   print("lose")
                   bal = balposazce
                   print("aktualni balance:",bal, "$")
                   volbaopak = "ano"
               else:
                        print("draw a card or hold?")
                        print("1.draw a card then hold")
                        print("2.hold")
                        volbacardhold = int(input(">"))
                        match volbacardhold:
                           case 1:
                               #tri karty a potom hold
                               #secteni 3 karet
                               print(firstcardplayer, secondcardplayer, thirdcardplayer)
                               print("součet tvých karet", firstcardplayer + secondcardplayer + thirdcardplayer)
                               print(firstcardpc + secondcardpc)
                               print("součet karet dealera", firstcardpc + secondcardpc)
                               logika()
                                    
                           case 2:
                                #hold s dvema kartama
                                print(firstcardplayer, secondcardplayer)
                                print("součet tvých karet", firstcardplayer + secondcardplayer)
                                print(firstcardpc + secondcardpc)
                                print("součet karet dealera", firstcardpc + secondcardpc)
                                logika()
                           case _:
                                print("pouze cisla 1-2")

                
           
       
            
            
            


            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        case _:
            print("pouze čísla")
            volbaopak == "ano"        


#karty:
    # normalni: 2-10
    # kral, kralovna, zolik: 10
    # eso: 1 nebo 11

# typy vyhry:
#     vic jak dealer ale nemas 21: $100 (original bet) + $100 (winnings) = $200 total
#     hitnes blackjack:  $100 (original bet) + $150 (winnings) = $250 total
#     remiza:$100 (original bet) = $100 total
                






