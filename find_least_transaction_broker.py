from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
# from scipy import stats
from statistics import mode
import retrieve_from_mongo as apple

# because this is in the same folder we don't have to make a package and module and can directly call it
df = apple.this_frame
df1 = df.drop('Contract_No', axis=1).drop(['Buyer_Broker', 'Seller_Broker', 'Date'], axis=1).groupby(
    'Stock_Symbol').describe()

# this is for an individual ticker
put_the_stock_name = 'NABIL'  # enter the stock name you want to search
put_the_stock_quantity = 10  # adjust quantity here accordingly

shay = df[df['Quantity'].apply(lambda x: x == put_the_stock_quantity)]
shady_brokers = shay[['Stock_Symbol', 'Quantity', 'Buyer_Broker', 'Seller_Broker', 'Rate', 'Date']]
shady_brokers1 = shady_brokers.reset_index().drop(['index'], axis=1).groupby('Stock_Symbol', sort=True)
shayshay = shady_brokers.groupby('Stock_Symbol')



dictionary_of_brokers = {}


def to_zip_the_brokers_name():
    global dictionary_of_brokers
    reading = pd.read_csv(r'C:\Users\Dell\Anaconda3\Nepse_Scraping_till_retreiving_from_mongo\broker_list.csv')
    reading.columns = ['Stock_Broker', 'Broker_Number']
    # reading.set_index('Broker_Number', inplace=True)
    just_one = reading['Broker_Number']
    just_one_list = list(just_one)
    just_two = reading['Stock_Broker']
    just_two_list = list(just_two)
    zipping = zip(just_one_list, just_two_list)
    dictionary_of_brokers = dict(zipping)


to_zip_the_brokers_name()


# call this function if you want to see the brokers that have been trading 10 scripts for the specific company
def buyer_broker_and_seller_broker_for_specific_ticker_for_given_number_of_scripts():
    shady_brokersfin = shayshay.get_group(put_the_stock_name).set_index(
        np.arange(1, len(shayshay.get_group(put_the_stock_name)) + 1))
    most_repeated_buyer_broker_for_individual_ticker = str(mode(shady_brokersfin['Buyer_Broker']))
    most_repeated_seller_broker_for_individual_ticker = str(mode(shady_brokersfin['Seller_Broker']))
    print('The most repeated seller broker for {} only in {} scripts is:'.format(put_the_stock_name,put_the_stock_quantity),
          dictionary_of_brokers[most_repeated_seller_broker_for_individual_ticker])
    print('The most repeated buyer broker for {} only in {} scripts is:'.format(put_the_stock_name,put_the_stock_quantity),
          dictionary_of_brokers[most_repeated_buyer_broker_for_individual_ticker])


# call this is you want to see the brokers that have been trading 10 scripts for all companies
def all_tickers_repeated_broker_for_given_number_of_scripts():
    sorted_minimal_transaction = shady_brokers.sort_values(['Stock_Symbol', 'Date'], ascending=[True, True])
    most_repeated_broker = mode(sorted_minimal_transaction['Seller_Broker'])
    most_repeated_broker_str = str(most_repeated_broker)

    print('The most repeated buyer broker for all tickers of {} scripts is:'.format(put_the_stock_quantity),
          dictionary_of_brokers[most_repeated_broker_str])


# call this function if you want to see the detailed description for the particular company
def most_transacted_brokers_for_the_given_stock_ticker():
    filter_by_name_data_frame = df[df['Stock_Symbol'].apply(lambda x: x == put_the_stock_name)]
    filter_by_name_data_frame = filter_by_name_data_frame.groupby('Buyer_Broker').describe()
    this_frame223 = filter_by_name_data_frame
    contract_number_count = this_frame223['Contract_No']['count']
    contract_number_count.columns = ['Number_of_contracts']
    contract_number_count = pd.DataFrame(contract_number_count)
    quantity_from_filter_by_this_frame = this_frame223['Quantity']
    quantity_from_filter_by_this_frame = quantity_from_filter_by_this_frame[['min', 'mean', 'max']]
    quantity_from_filter_by_this_frame.columns = ['Quantity/min', 'Quantity/mean', 'Quantity/max']
    rate_from_filter_by_this_frame = this_frame223['Rate']
    rate_from_filter_by_this_frame = rate_from_filter_by_this_frame[['min', 'mean', 'max']]
    rate_from_filter_by_this_frame.columns = ['Rate/min', 'Rate/mean', 'Rate/max']
    main_list_for_most_transacted = contract_number_count.join(quantity_from_filter_by_this_frame)
    main_list_for_most_transacted = main_list_for_most_transacted.join(rate_from_filter_by_this_frame)
    return main_list_for_most_transacted


buyer_broker_and_seller_broker_for_specific_ticker_for_given_number_of_scripts()
all_tickers_repeated_broker_for_given_number_of_scripts()
description_of_particular_ticker = most_transacted_brokers_for_the_given_stock_ticker()
