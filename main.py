import pprint
import pandas as pd
import datetime
import json

ff = r'C:\Users\Artur\macro\macroslibrary.csv'
df = pd.read_csv(ff)
#print(df)
print(df)

x = float(input('c'))
y = float(input('s'))


def cena(self, prs):
    self.prs = prs
    pr = df['Cena'][x]
    prs = pr/(s/y)
    

def size(self, s):
    self.s = s
    s = df['Size/g'][x]
    
    


def fat(self, fa):
    self.fa = fa
    f = df['Fat/100g'][x]
    fa = f*(y/100)
    

def carbs(self, ca):
    self.ca = ca
    c = df['Carbs/100g'][x]
    ca = c*(y/100)
    

def protein(self, pro):
    self.pro = pro

    p = df['Protein/100g'][x]
    pro = p*(y/100)
    
def calories(self,kcal):
    self.kcal = kcal
    kcal = (protein() * 4)+(carbs()*4)+(fat()*9)
    



'''def get_macros(self , data):
    return_list = []
    for entry in data[df['Product'][x]]:
        return_list.append (
            
                prices = entry['prices'],
                fats = entry['fat'],
                carbs = entry['carbs'],
                proteins = entry['carbs'],
                calories = entry['calories'],
            
        )
'''
class Macros:
    def __init__(self, prs, fa, ca,pro,calories):
        self.prs = prs
        self.fa = fa
        self.ca = ca
        self.pro = pro
        self.calories = calories
    
    
    
    def serialize(self):
        return{
            'prices' : self.prs,
            'fats' : self.fa,
            'carbs' : self.ca,
            'proteins' : self.pro,
            'calories' : self.calories,
        }
    
        
        
a = serialize()
with open('record.json', 'w') as json_file:
    json.dump(a, json_file, sort_keys=True, indent=4)

print(a)