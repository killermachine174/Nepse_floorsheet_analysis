import pandas as pd
from pymongo import MongoClient
from datetime import datetime
client = MongoClient()  # for data base
db = client.NEPSE_FloorSheet  # for data base
test = list(db['nepse'].find({},{'_id':0})) #this is cause you do not want the id.
data_frame = pd.DataFrame(test)
amount_list = []
all_datas = []
#print(data_frame.columns)
for column in data_frame.columns:
    all_datas.append([item for sublist in data_frame[column] for item in sublist]) #list comprehension. Go to google image and there will be one that will explain this

rate_dict = {'Contract_No':all_datas[1],'Stock_Symbol':all_datas[2],'Buyer_Broker':all_datas[3],
             'Seller_Broker':all_datas[4],'Quantity':all_datas[5],'Rate':all_datas[6],'Amount':all_datas[7],'Date': all_datas[8]}
this_frame = pd.DataFrame.from_dict(rate_dict)
