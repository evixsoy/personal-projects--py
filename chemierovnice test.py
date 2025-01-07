vzorecky = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
err = 0
counterleft = {}
counterright = {}

left = "H2O + C2H6"
right = "Ag2 + CO2"
elementsleft = []
elementsright = []
foundleft = []
foundright = []
step = 1
testleft = []
testright = []


#dat elementy do listu left
for z in left:
    if z in " " or z in "+":
        pass
    else:
        elementsleft.append(z)
elementsleftlen = len(elementsleft)
for i in range(0,elementsleftlen): 
    num = 1
    if elementsleft[i].isupper() and elementsleft[i+1].islower() and elementsleft[i+2].isdigit():
        checkelement = elementsleft[i] +elementsleft[i+1]
        num = int(elementsleft[i+2])
    elif elementsleft[i].isupper() and elementsleft[i+1].islower():
        checkelement = elementsleft[i] +elementsleft[i+1]
        num = 1
    elif elementsleft[i].isupper() and elementsleft[i+1].isdigit():
        checkelement = elementsleft[i]
        num = int(elementsleft[i+1])
    elif elementsleft[i].isupper():
        checkelement = elementsleft[i] 
        num = 1
    testleft.append(checkelement)
    if i ==0 or testleft[i-1] != testleft[i]:
        for j in counterleft:
            if j == checkelement:
                num = counterleft[checkelement] + num 
        foundleft.append(checkelement)
        counterleft[checkelement] = num 
    elif testleft[i-1] == testleft[i]:
        pass
print(counterleft)

# dat elementy do listu right

for z in right:
    if z in " " or z in "+":
        pass
    else:
        elementsright.append(z)
elementsrightlen = len(elementsright)
for i in range(0,elementsrightlen): 
    num = 1
    if elementsright[i].isupper() and elementsright[i+1].islower() and elementsright[i+2].isdigit():
        checkelement = elementsright[i] +elementsright[i+1]
        num = int(elementsright[i+2])
    elif elementsright[i].isupper() and elementsright[i+1].islower():
        checkelement = elementsright[i] +elementsright[i+1]
        num = 1
    elif elementsright[i].isupper() and elementsright[i+1].isdigit():
        checkelement = elementsright[i]
        num = int(elementsright[i+1])
    elif elementsright[i].isupper():
        checkelement = elementsright[i] 
        num = 1
    testright.append(checkelement)
    if i ==0 or testright[i-1] != testright[i]:
        for j in counterright:
            if j == checkelement:
                num = counterright[checkelement] + num 
        foundright.append(checkelement)
        counterright[checkelement] = num 
    elif testright[i-1] == testright[i]:
        pass

print(counterright)