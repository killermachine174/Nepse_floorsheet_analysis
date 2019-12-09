The order in which the files should be run are as follows:
1) NEPSE Floorsheet-24th Sept 2019-to scrape data for a particular day (use fake useragent to remain anonymous)
2) If needed: run "to adjust date"
3) Save the Nepsefloor sheet locally as csv and name it with "set_date_time_for_naming"
4) To put files in Mongo DB
5) Retreive from Mongo files
6) To make a list of broker's list run Broker_list_scrape and save it locally as "broker_list.csv"
7) To find out name of brokers use the find_least_transaction_broker.py
8) Plot the data
* Note: there are additional files that you dont need to run but will be called fake_useragent is one of them
* if you scrape the floorsheet the next day run to adjust the date file for the required csv to have its date coulmn updated before it is put in Mongo
