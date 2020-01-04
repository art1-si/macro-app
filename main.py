import pprint
import pandas as pd
import datetime
from datetime import date
import json
from app import *
import os

date_time = date.today()
start_time = datetime.datetime.now()
activeList = AcitivyList([])
activeList.initialize_me()




calculate_macros = Macros(start_time,s,pr,f,c,p,0)
calculate_macros.calc()
activity = Activity(product, [calculate_macros])
activeList.activities.append(activity)
with open(('record/Macro_from_{}.json'.format(date_time.strftime("%Y-%m-%d"))), 'w') as json_file:
    json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)
#activity = Macro(activity_name, [time_entry])
print(calculate_macros.serialize())

   
#





