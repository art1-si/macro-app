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
    prs = pr/(size()/y)
    return prs

def size():
    s = df['Size/g'][x]
    
    return s


def fat():
    f = df['Fat/100g'][x]
    fa = f*(y/100)
    return fa

def carbs():
    c = df['Carbs/100g'][x]
    ca = c*(y/100)
    return ca

def protein():
    p = df['Protein/100g'][x]
    pro = p*(y/100)
    return pro
def calories():
    kcal = (protein() * 4)+(carbs()*4)+(fat()*9)
    return kcal



def serialize():
        return {
            'prices' : cena(),
            'fats' : fat(),
            'carbs' : carbs(),
            'proteins' : protein(),
            'calories' : calories(),
            

        }
a = serialize()
with open('record.json', 'w') as json_file:
    json.dump(a, json_file, sort_keys=True, indent=4)

print(a)
