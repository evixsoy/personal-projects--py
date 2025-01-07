import datetime
import os 

err = 0
middays = [4,6,9,11]
prestuprok = 0
count = 0
found = 0
foundplace = 0
opakovani = 1
zobr = 0
err = 0

while opakovani ==1:
    print("1. napsat nove heslo")
    print("2. podivat se na seznam")
    choice = int(input())
    match choice:
        case 1:
            name = str(input("name:"))
            day = int(input("day:"))
            month = int(input("month:"))
            year = int(input("year:"))
            #prestupny rok
            vypocet = year/4
            if vypocet.is_integer():
                prestuprok = 1

            #restrictions
            if day > 31 or day<1 or month > 12 or month<1 or year > 2024 or year<1900:
                err = 1

            if month in middays and day>30:
                err = 1

            if prestuprok ==1 and day> 29 and month ==2 or prestuprok ==0 and day> 28 and month ==2:
                err =1

            if err==1:
                print("spatny format")
            else:
                with open("date.env","a") as datewrite:
                    datewrite.write(f"{day}/{month}|")
                with open("name.env","a") as namewrite:
                    namewrite.write(f"{name}|")
                with open("year.env","a") as yearwrite:
                    yearwrite.write(f"{year}|")

        case 2:
            
            with open("date.env") as dateopen:
                filefinddate = dateopen.read()
                datelist =filefinddate.split("|")
            with open("name.env") as nameopen:
                filefindname = nameopen.read()
                namelist =filefindname.split("|")
            with open("year.env") as yearopen:
                filefindyear = yearopen.read()
                yearlist =filefindyear.split("|")

            for i in range(0,len(datelist)-1):
                print(f"{namelist[i]}: {datelist[i]}/{yearlist[i]}")