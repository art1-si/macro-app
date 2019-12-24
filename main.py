import pprint
import pandas as pd
import datetime
import json

ff = r'C:\Users\Artura\pythProjects\MacrosApp\Macroslibrary.csv'
df = pd.read_csv(ff)
#print(df)
print(df)

x = float(input('c'))
y = float(input('s'))
def cena():
    pr = df['Cena'][x]
    return pr

def size():
    s = df['Size/g'][x]
    return s


def fat():
    f = df['Fat/100g'][x]
    return f

def carbs():
    c = df['Carbs/100g'][x]
    return c

def protein():
    p = df['Protein/100g'][x]
    return p

def calc():
    prs = cena()/(size()/y)
    print('Prices:',prs)
    fa = fat()*(y/100)
    print('Fat: ',fa)
    ca = carbs()*(y/100)
    print('Carbs: ',ca)
    pro = protein()*(y/100)
    print('Proteins: ',pro)
    kcal = (pro * 4)+(ca*4)+(fa*9)
    print('Kcal: ',kcal)
    
    

calc()


