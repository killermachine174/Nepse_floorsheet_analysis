# remember there are 3 ways of plotting data
''''
1) To create a function figure like
figure1 = plt.figure()
axes1=figure1.add_axes([0,0,1,1])
axes1.plot(x,y,color='black',linewidth = 2, alpha = 0.5,ls='-',marker = "D",mfc = 'black') #you can put any rgb hex codes
#instead of linewidth you can also write lw
axes1.set_xlim(0,5)
axes1.set_ylim(0,5)

2) Create a subplot like
f2,ax2 = plt.subplots(1,1, figsize=(16,7))

3) Plot straight through pandas
dfx.plot.hexbin(x='A',y='B',gridsize=20,cmap='coolwarm')'''

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
#from scipy import stats
from statistics import mode
import retrieve_from_mongo as apple  # becuase this is in the same folder we don't have to make a package and module and can directly call it
import Broker_list_scrape as orange

df = apple.this_frame
df1 = df.drop('Contract_No', axis=1).drop(['Buyer_Broker', 'Seller_Broker', 'Date'], axis=1).groupby(
    'Stock_Symbol').describe()

shay = df[df['Quantity'].apply(lambda x: x ==10)]
shady_brokers = shay[['Stock_Symbol', 'Quantity', 'Buyer_Broker', 'Seller_Broker', 'Rate', 'Date']]
shady_brokers1 = shady_brokers.reset_index().drop(['index'], axis=1).groupby('Stock_Symbol', sort=True)
shayshay = shady_brokers.groupby('Stock_Symbol')

# this is for an individual ticker
put_the_stock_name = 'NABIL'  # enter the stock name you want to search
shady_brokersfin = shayshay.get_group(put_the_stock_name).set_index(
    np.arange(1, len(shayshay.get_group(put_the_stock_name)) + 1))
most_repeated_broker_for_individual_ticker = str(mode(shady_brokersfin['Buyer_Broker']))
print('The most repeated buyer broker for {} is:'.format(put_the_stock_name),orange.dictionary_of_brokers[most_repeated_broker_for_individual_ticker])

#this is for all the transaction
sorted_minimal_transaction = shady_brokers.sort_values(['Stock_Symbol', 'Date'], ascending=[True, True])
most_repeated_broker = mode(sorted_minimal_transaction['Buyer_Broker'])
most_repeated_broker_str = str(most_repeated_broker)
print('The most repeated buyer broker for all transaction is:',orange.dictionary_of_brokers[most_repeated_broker_str])
