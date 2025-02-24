#test -> nejak dobre to nefunguje (mozna nekdy dodelam)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

koef = [2,4,6] #muze se zmenit
tabx = [-2,-1,-0.5,0.5,1,2] #muze se zmenit

def calculate(tabx,koef):
    values = {}
    for i in koef:
        radek = []
        for g in tabx:
            radek.append(g**i)
        values[i] = radek
    return values

def gentab(koef,tabx):
    data = calculate(tabx,koef)
    df = pd.DataFrame(data.values(), columns=tabx, index=koef)
    return df

# print(gentab(koef,tabx))
data = calculate(tabx,koef)


fig, ax = plt.subplots()
ax.set_xlim(-8, 8)  #variable
ax.set_ylim(0, 10) # variable  

count = 0
for i in data.keys():
    for g in tabx:
        ax.scatter(g, min(data[i][count], 100), color='red', label="Body") #variable
        if count == len(tabx)-1:
            count= 0
            ax.plot(tabx, [min(y, 100) for y in data[i]], label="Spojovací čára", color='blue') #variable
        else: 
            count+=1

ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
plt.show()

#TODO NEFUNGUJE min u 3,4 (blbe se spojuje -> asi u ax.plot chyba)
