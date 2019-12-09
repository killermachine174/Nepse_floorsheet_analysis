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
from find_least_transaction_broker import df as main_data_frame
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from find_least_transaction_broker import dictionary_of_brokers

to_be_used_data_frame = main_data_frame[main_data_frame['Buyer_Broker'].apply(lambda x: x == 22)]
# to_be_used_data_frame1 = main_data_frame[main_data_frame['Stock_Symbol'].apply(lambda x: x == 'PRVU')]
first_data_frame = to_be_used_data_frame.groupby('Stock_Symbol').sum()

print(first_data_frame)
first_data_frame = first_data_frame['Quantity']
second_data_frame = pd.DataFrame(first_data_frame)
second_data_frame = second_data_frame.reset_index()

second_data_frame.to_excel(r'C:\Users\Dell\Desktop\Siprabi.xlsx')
#plotting
fig = plt.figure(dpi=100, figsize=(50,50)) #if you are showing the plt then adjust to 50,50
axes = fig.add_axes([0.1, 0.1, 0.9, 0.8])  # the two 0.1 is the left corner and then the width and the height
axes.bar(second_data_frame['Stock_Symbol'], second_data_frame['Quantity'], color='blue')

axes.set_title('Number of Quantity Traded', fontsize=100, loc='center')
axes.set_xlabel('Company Name', fontsize=100)
axes.set_ylabel('Number of Quantity Traded', fontsize=100)
axes.tick_params(axis="x", labelsize=30)
axes.tick_params(axis="y", labelsize=50)
plt.xticks(rotation=75)
plt.show()
# plt.savefig('Stock_market.png')