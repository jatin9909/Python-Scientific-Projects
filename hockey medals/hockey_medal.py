import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import MaxNLocator
import pandas as pd
import math
 
# y-axis in bold
rc('font', weight='bold')
 
# Values of each group
bars1 = [3,6,5,7,4,2,1,0,2,0,0,0,1,0,0,0,0,2,2,1]
bars2 = [1,6,4,2,2,3,3,3,3,0,0,3,1,1,1,1,1,0,0,0]
bars3 = [8,6,4,4,4,3,1,1,1,1,1,0,1,0,0,0,0,0,0,0]
summ  = [13,18,13,13,10,8,5,4,6,1,1,3,3,1,1,1,1,2,2,1]
 
# Heights of bars1 + bars2
bars = np.add(bars1, bars2).tolist()
 
# The position of the bars on the x-axis
r = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
 
# Names of group and bar width
names = ['India','Netherlands','Australia','Great Britain','Germany','Pakistan','Spain','West Germany','Argentina','New Zealand','Zimbabwe','South Korea','Belgium','China','Czechoslovakia','Denmark','Japan','Soviet Union','United States','UTG']
barWidth = 1
 
# Create brown bars
plt.bar(r, bars1, color='#cd7f32', edgecolor='white', width=barWidth)
# Create green bars (middle), on top of the first ones
plt.bar(r, bars2, bottom=bars1, color='#C0C0C0', edgecolor='white', width=barWidth)
# Create green bars (top)
plt.bar(r, bars3, bottom=bars, color='#FFD700', edgecolor='white', width=barWidth)
 
# Custom X axis
plt.xticks(r, names, fontweight='bold',rotation=60,horizontalalignment='right')


#Cutom Y axis
plt.ylabel("Number of Medals")

low = min(summ)
high = max(summ)
new_list = range(math.floor(min(summ)), math.ceil(max(summ))+1)
plt.yticks(new_list)

#title
plt.title("All medals won by nation in field hockey Men and Women from 1908 to 2020 olympics",fontsize="18")
 
#legend
colors=['Bronze','Silver','Gold']
plt.legend(colors,loc=1)

# Show graphic
plt.grid(axis='y')
plt.show()