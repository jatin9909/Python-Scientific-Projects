import random
import pandas as pd
import matplotlib.pyplot as plt

# Import Data
df_raw = pd.read_csv("extractdata.csv")

# Prepare Data
df = df_raw.groupby('UploadYear').size().reset_index(name='counts')
#print(df) print years with count
n = df['UploadYear'].unique().__len__() # total 14
#print(n)

all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)
#print(c)

# Plot Bars
plt.figure(figsize=(16,10), dpi= 80)
plt.bar(df['UploadYear'], df['counts'], color=c, width=.5)
for i, val in enumerate(df['counts'].values):
	plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})

# Decoration
plt.gca().set_xticklabels(df['UploadYear'],rotation=60, horizontalalignment= 'right')
plt.title("Number of videos having more than 1 Billion view in each year", fontsize=22)
plt.ylabel('# Number of videos have more than 1 billion views')
plt.ylim(0, 45)
plt.show()
