import os
import time
symbol = "*"
space = " "

def pattern1():
    for i in range(1,6):
        vysledek = symbol * i 
        print(f"{vysledek}")

def pattern2():
   for i in range(5,0, -1):
    vysledek = symbol * i 
    print(f"{vysledek}")

def pattern3():
    for i in range(1,6):
        if i == 1 or i ==5:
            print(symbol * 5)
        else:
            print(symbol, space * 1, symbol)

def pattern4():
    x = 5
    for i in range(1,10,2):
        print(x*space, i*symbol, x*space)
        x = x-1
    x = 2
    for j in range(7,0,-2):
        print(x*space, j*symbol, x*space)
        x = x+1

def pattern5():
    x = 4
    for i in range(3,6,2):
        print(space*(x//2), symbol*i, space*(x//4), symbol*i,space*(x//2))
        x = x-2
    x = 0
    for j in range(15,0,-2):
        print(space*x, symbol*j,space*x )
        x= x+1

def pokracovani():
    print("1. menu")
    print("2. end")
    pokracovani = int(input())
    match pokracovani:
        case 1:
            os.system("cls")
            pass
        case 2:
            os._exit(0)

while True:
    os.system("cls")
    print("vyber pattern:")
    print("1. pattern:")
    print("2. pattern:")
    print("3. pattern:")
    print("4. pattern:")
    print("5. pattern:")
    volba = int(input(">"))
    match volba:
        case 1:
            os.system("cls")
            pattern1()
            pokracovani()
        case 2:
            os.system("cls")
            pattern2()
            pokracovani()
        case 3:
            os.system("cls")
            pattern3()
            pokracovani()
        case 4:
            os.system("cls")
            pattern4()
            pokracovani()
        case 5:
            os.system("cls")
            pattern5()
            pokracovani()
        case _:
            print("spatny input")
            time.sleep(1)
