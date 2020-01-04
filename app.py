import pandas as pd
import json
import datetime
from datetime import date
from dateutil import parser
import os
ff = r'C:\Users\Artura\pythProjects\macro\macroslibrary.csv'
df = pd.read_csv(ff)
#print(df)
print(df)
start_time = datetime.datetime.now()
x = float(input('Row: '))
y = float(input('Size: '))
time = datetime.datetime.now()
date_time = date.today()
class AcitivyList:
    def __init__(self, activities):
        self.activities = activities
    
    def initialize_me(self):
        activity_list = AcitivyList([])
        
        if not os.path.exists('record/Macro_from_{}.json'.format(date_time.strftime("%Y-%m-%d"))):
            with open('record/Macro_from_{}.json'.format(date_time.strftime("%Y-%m-%d")), 'w'):
                pass
        else:
            with open(('record/Macro_from_{}.json'.format(date_time.strftime("%Y-%m-%d"))), 'r') as f:
                data = json.load(f)
                activity_list = AcitivyList(
                    activities = self.get_activities_from_json(data)
                )
            return activity_list
    
    def get_activities_from_json(self, data):
        return_list = []
        for activity in data['activities']:
            return_list.append(
                Activity(
                    name = activity['Product'],
                    time_entries = self.get_time_entires_from_json(activity),
                )
            )
        self.activities = return_list
        return return_list
    
    def get_time_entires_from_json(self, data):
        return_list = []
        for entry in data['Macros']:
            return_list.append(
                Macros(
                    time_added = parser.parse(entry['added at']),
                    s = entry['size'],
                    pro = entry['proteins'],
                    prs = entry['prices'],
                    fa = entry['fats'],
                    ca = entry['carbs'],
                    calories = entry['calories'],
                )
            )
        self.time_entries = return_list
        return return_list
    
    def serialize(self):
        return {
            'activities' : self.activities_to_json()
        }
    
    def activities_to_json(self):
        activities_ = []
        print('adad')
        for activity in self.activities:
            activities_.append(activity.serialize())
        
        return activities_


class Activity:
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries

    def serialize(self):
        return {
            'Product' : self.name,
            'Macros' : self.make_time_entires_to_json()
        }
    
    def make_time_entires_to_json(self):
        time_list = []
        for time in self.time_entries:
            time_list.append(time.serialize())
        return time_list





class Macros:
    def __init__(self,time_added,s , prs, fa, ca,pro,calories):
        self.time_added = time_added
        self.s = s
        self.prs = prs
        self.fa = fa
        self.ca = ca
        self.pro = pro
        self.calories = calories
    
    def calc(self):
        global y  
                
        self.prs = self.prs/(self.s/y)          
        self.fa = self.fa*(y/100)        
        self.ca = self.ca*(y/100)       
        self.pro = self.pro*(y/100)
        self.calories = (self.pro * 4)+(self.ca * 4) + (self.fa * 9)
        print('sdsd')

    def serialize(self):
        return{
            'added at': self.time_added.strftime("%Y-%m-%d %H:%M:%S"),
            'size' : y,
            'prices' : self.prs,
            'fats' : self.fa,
            'carbs' : self.ca,
            'proteins' : self.pro,
            'calories' : self.calories,
        }
    
       # self.calories = calories
       #calories = (self.pro * 4)+(self.ca*4)+(self.fa*9)
       # print('adsds')
    
    '''def serialize(self):
        return{
            'prices' : self.prs,
            'fats' : self.fa,
            'carbs' : self.ca,
            'proteins' : self.pro,
            #'calories' : self.calories,
        }'''

product = df['Product'][x]
pr = df['Cena'][x] 
s = df['Size/g'][x]   
f = df['Fat/100g'][x] 
c = df['Carbs/100g'][x]  
p = df['Protein/100g'][x]
