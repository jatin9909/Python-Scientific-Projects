import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

data = pd.read_csv('stats.csv')
# names = list(data['Prime_Minister'])
# words = list(data['Words'])

names = ['Gulzarilal Nanda' ,'Chandra Shekhar ','Charan Singh' ,'H.D. Deve Gowda' ,'Morarji Desai' ,'Inder Kumar Gujral' ,'Vishwanath Pratap Singh' ,'Manmohan Singh' ,'Lal Bahadur Shastri' ,'P.V. Narasimha Rao' ,'Rajiv Gandhi' ,'Atal Bihari Vajpayee' ,'Narendra Modi' ,'Indira Gandhi' ,'Jawaharlal Nehru']
words = [863,1620,1896,1907,2302,2797,4536,4678,5361,5416,5446,6859,10664,12790,13683]


fig,ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)


plt.barh(names,words,0.5)


plt.xlabel('Wikipedia word count')
plt.title('Indian Prime Ministers according to the word count of their wikipedia page')
for index, value in enumerate(words):
    plt.text(value, index, str(value),va='center')
plt.show()