# u 3. passgen dat loop

import random

checkuser = []
opak = 0
velka = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cisla = [1,2,3,4,5,6,7,8,9]
password = ""

def passgen():
    password = ""
    for i in range(15):
        num = random.randint(1,99)
        if num <=33:
            znak = random.choice(velka)
        elif num <=66 :
             znak = random.choice(lowercase)
        elif num <=99:
            znak = str(random.choice(cisla))
        password = password + znak   
    return password


while True:
    print("---Keygen---")
    print("1.register")
    print("2.login")
    print("3.passgen")
    print("------------")
    volbalogin = int(input(">"))
    match volbalogin:
        #registrace 
        case 1:
            print("napis uz.jmeno")
            uzjmeno = input(">")
            print("napis heslo")
            uzheslo = input(">")
            filelogin = open("login.env", "w")
            filelogin.write(f"{uzjmeno} {uzheslo}")
            with open("pass.env", "w") as filedelete:
                 filedelete.write("")
        #login
        case 2:
            print("napis uz.jmeno")
            uzjmenologin = input(">")
            checkuser.append(uzjmenologin)
            print("napis heslo")
            uzheslologin = input(">")
            checkuser.append(uzheslologin)

            with open("login.env", "r") as filelogin:
                filelogin = str(filelogin.read())

            checkfile = filelogin.split(" ")

            if checkfile == checkuser:
                #menu 2
                print(True)
                checkuser = []
                print("---Vyber možnost:---")
                print("---1.vytvořit nové heslo---")
                print("---2. podívat se na stálá hesla---")
                volbaheslo = int(input(">"))
                match volbaheslo:
                    #create pass
                    case 1:
                        while opak ==0:
                            username = str(input("uzivatelske jmeno:"))
                            print("---Jak chceš zadat heslo?---")
                            print("---1.napsat své heslo---")
                            print("---2. vygenerovat heslo---")
                            passgenchoice = int(input(">"))
                            match passgenchoice:

                                case 1:
                                    heslo = str(input("heslo:"))

                                case 2:
                                    heslo = passgen()

                            with open("pass.env", "a") as filepass:
                                filepass.write(f"username: {username} password: {heslo}\n")
                                
                            #menu 3
                            print("1.dalsi pass")
                            print("2.menu")
                            volba2= int(input())

                            match volba2:
                                case 1:
                                    opak = 0

                                case 2:
                                    opak = 1
                    # show previous pass
                    case 2:
                        with open("pass.env", "r") as filepass:
                            print(filepass.read())

            else:
                print(False)
        case 3:
            print(passgen())
