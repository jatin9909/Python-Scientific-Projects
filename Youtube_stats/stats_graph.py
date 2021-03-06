import random
import pandas as pd
import matplotlib.pyplot as plt

# Import Data
df_raw = pd.read_csv("Youtube_videos_more_than_1Billion_views.csv")

# Prepare Data
df = df_raw.groupby('UploadYear').size().reset_index(name='counts')
print(df)
#print(df) print years with count
n = df['UploadYear'].unique().__len__() # total 14
#print(n)

all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)
#print(c)

# Plot Bars
plt.figure(figsize=(16,10), dpi= 80)
plt.bar(df['UploadYear'], df['counts'], color=c, width=.6)

for i, val in enumerate(df['counts'].values):
	plt.text(i, val, '%d'%int(val),horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':20})

# Decoration

plt.xticks(df['UploadYear'],fontsize=18)
plt.title("All YouTube videos with more than 1 Billion views uploads in which year", fontsize=22)
plt.ylabel('# Number of videoss',fontsize=18)
plt.ylim(0, 45)
plt.show() 
