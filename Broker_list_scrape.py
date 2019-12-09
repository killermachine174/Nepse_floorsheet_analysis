#please use this file to get the csv list of brokers only
#once the list has been obtained this file is no longer necessary
#the code has already been embedded in find_least_transaction_broker
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import fake_useragent as orange

URL = 'https://merolagani.com/BrokerList.aspx'
requesting = requests.get(URL)
souped = BS(requesting.content, 'html.parser')
finding_out_the_table = souped.find(class_='table table-striped table-hover')
table_row = finding_out_the_table.find_all('tr')
all_data = []
for single_row in table_row:
    table_data = single_row.find_all('td')
    single_row_data = [i.text.strip() for i in table_data]
    all_data.append(single_row_data)
# the code above works fine
all_data2 = all_data[1:]
# All fine till here as well

length_of_the_list = len(all_data2)
length_counter = 0
number_and_name_of_brokers = []
number_only=[]
name_only=[]
while length_counter < length_of_the_list:
    pop_list = all_data2[length_counter]
    number_and_name_of_brokers.append(pop_list[0:2])
    number_only.append(pop_list[0])
    name_only.append(pop_list[1])
    length_counter=length_counter+1
#Code good till here

# zipping = zip(number_only,name_only)
# dictionary_of_brokers = dict(zipping)
dataframe_of_brokers= pd.DataFrame(number_only,name_only)
dataframe_of_brokers.to_csv(r'C:\Users\Dell\Anaconda3\Nepse_Scraping_till_retreiving_from_mongo\broker_list.csv')
#print(dictionary_of_brokers)
#Code works and checked

