# for multiple pages
import requests
import pandas as pd
from bs4 import BeautifulSoup as BS
from datetime import datetime
import fake_useragent as orange
def page_number_getter():
    UURL = 'http://www.nepalstock.com/main/floorsheet/index/0/'
    first_requesting= requests.get(UURL, headers=orange.random_headers())
    first_souped= BS(first_requesting.content,'html.parser')
    #to find colspan ='7' because it is where the Last button is
    colspan = first_souped.find(colspan='7')
    #print(colspan)
    all_a_tags = colspan.find_all('a')[-1]
    this_href= all_a_tags.get('href')
    splitted_href = this_href.split('/')
    wanted_href = splitted_href[-2]
    return(int(wanted_href)+1)

all_rows = []
for page in range(1,page_number_getter()): #put the page number till which you want to scrape
    # requesting and parsing html
    URL = 'http://www.nepalstock.com/main/floorsheet/index/{}'.format(page)
    requesting = requests.get(URL)
    souped = BS(requesting.content, 'html.parser')

    # to get the table
    table = souped.find('tbody')

    # to get the table rows
    table_rows = souped.find_all('tr')

    all_headings = ['S.N', 'Contract_No', 'Stock_Symbol', 'Buyer_Broker', 'Seller_Broker', 'Quantity', 'Rate', 'Amount']

#this is a useful function index and ennumerate

    for index, single_row in enumerate(table_rows):
#we are not taking the below mentioned index cause there are additional information there and we dont want that
        if index != 0 and index != 1 and index != 23 and index != 22 and index != 24:
            table_data = single_row.find_all('td')
            single_row_data = [i.text.strip() for i in table_data]
            all_rows.append(single_row_data)
    # print(all_rows)

    nepse_floorsheet = pd.DataFrame(all_rows, columns=all_headings)
nepse_floorsheet.set_index('S.N', inplace=True)
# this is the export to csv

for items in nepse_floorsheet:
    nepse_floorsheet['Date'] = datetime.now()
nepse_floorsheet1=nepse_floorsheet[0:-3]
nepse_floorsheet1.to_csv('dfloorsheet_csv/14th_Oct_2019.csv') #place the name of the csv file you want



