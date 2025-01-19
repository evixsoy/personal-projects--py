#nedodelany
# nefunguje asi jenom hledani jestli nema ucitel ve stejnou dobu 2 hodiny
# strasne zamotanej kod
# treba to nekdy dodelam
# nemam na to skill jeste ig


import random
classes = ["1.A", "1.B", "2.A", "2.B", "3.A", "3.B"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
subjects = ["Math", "Physics", "Chemistry", "Biology", "History", "English", "Physical Education", "Art", "Spanish", "pg", "break", "czech"]
teachers = {"Novak": "Math","Svoboda": "Physics","Dvorak":"Chemistry", "Horak": "Biology","Zeleny": "History","Kovarik":"English","Prokop": "Physical Education","Pavlik" : "Art","Kokrspanel": "Spanish","Jeff" : "pg","Nikdo ": "break","Pavel" : "czech"}

#kolik hodin jakeho predmetu musi trida mit za tyden
subject_hours = {"Math": 5,"Physics": 3,"Chemistry": 3,"Biology": 3,"History": 2,"English": 4,"Physical Education": 3,"Art": 2,"Spanish": 3,"pg" : 3,"break" : 5,"czech" : 5}
subject_hours_check = {key: 0 for key in subject_hours}
subject_hours_temp = subject_hours.copy()

hours = 8
templist = []
schedule_check = {day: {hour: [] for hour in range(1, hours + 1)} for day in days}
print(schedule_check)
class NalezenDuplikat(Exception):
    pass
class NalezenPrekryvani(Exception):
    pass
#generovani hodin u jednotlive tridy
for i in classes:
    for g in days:
        #do listu se apenduje denni rozvrh (check na duplikaty v jednom dni)
        testlist = []
        count = 0   
        while count < hours:
            try:
                predmet = random.choice(subjects)
                if subject_hours[predmet] < 1:
                    continue
                if predmet in schedule_check[g][count + 1]:
                    raise NalezenPrekryvani
                testlist.append(predmet)
                
                if testlist.count(predmet) > 1:
                        raise NalezenDuplikat
                subject_hours_temp[predmet] -= 1
                subject_hours_check[predmet] += 1
                count +=1
                templist.append(f"Trida:{i}| Den: {g}| {count}.hodina: {predmet}")
                
                prekryvanicheck = []
                for p in templist:
                    prekryvanicheck.append(p.split("Den:")[1].strip())
                
                for r in prekryvanicheck:
                    if prekryvanicheck.count(r) > 2:
                        print("ano")
                        raise NalezenPrekryvani      
            except NalezenDuplikat:
                print("restart...")
                testlist.pop()
                continue
            except NalezenPrekryvani:
                print("restart...")
                templist.pop()
                continue
    sorted_hourscheck = {klic: subject_hours_check[klic] for klic in sorted(subject_hours_check.keys())}
    sorted_hours = {klic: subject_hours[klic] for klic in sorted(subject_hours.keys())}
    check = {}
    test = -1
    
    #nalezeni posledniho prvku
    for i in sorted_hours:
        posledni_prvek= i
    #check jestli se shoduje pocet hodin generovanyho rozvrhu s poctem hodin predmetu za tyden
    for i in sorted_hourscheck:
        test += 1

        if sorted_hourscheck[i] > sorted_hours[i]:
            rozdil = sorted_hourscheck[i] - sorted_hours[i]

            klice = list(sorted_hourscheck.keys())
            if test < len(klice) - 1:  
                sorted_hourscheck[klice[test]] -= rozdil       
                sorted_hourscheck[klice[test + 1]] += rozdil

        if sorted_hourscheck[i] < sorted_hours[i]:
            rozdil = sorted_hours[i] - sorted_hourscheck[i]

            klice = list(sorted_hourscheck.keys())
            if test < len(klice) - 1:  
                sorted_hourscheck[klice[test]] += rozdil       
                sorted_hourscheck[klice[test + 1]] -= rozdil
        if sorted_hourscheck[posledni_prvek] > sorted_hours[posledni_prvek]:
           sorted_hourscheck[posledni_prvek] = sorted_hours[posledni_prvek] 
dalsilist = []

for i in templist:
    for j in teachers.values():
        subject = i.split("|")[-1].split(":")[-1].strip()
        if subject == j:
            keys = [key for key, value in teachers.items() if value == j]
    dalsilist.append(keys)
pocet = 0

for i in templist:
    print(f"{i} : {dalsilist[pocet]}")
    pocet +=1


#TODO aby kazda trida mohla mit vlastni seznam ucitelu, pocet hodinu, predmetu apod
#TODO nesmi se prekryvat hodiny


