import pandas as pd
from pymongo import  MongoClient
from datetime import datetime
client = MongoClient() #for data base
db = client.NEPSE_FloorSheet #for data base
#please update your filename
floorsheet = pd.read_csv(r'C:\Users\Dell\Anaconda3\Nepse_Scraping_till_retreiving_from_mongo\dfloorsheet_csv\14th_Oct_2019.csv')#enter path name
floorsheet1 = floorsheet.to_dict('list') #please look up to_dict's methods. 'list is one of them
#floorsheet1["date"] = datetime.now() #instead of date time now I have updated something else in my program while scraping itself
db['nepse'].insert(floorsheet1, check_keys=False)
