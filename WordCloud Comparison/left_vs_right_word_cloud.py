import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

dataset = open("comments_left_final.txt", "r").read()
def create_word_cloud(string):
    # cloud = WordCloud(background_color = "white", max_words = 200)
    # cloud.generate(string)
    # cloud.to_file("left.png")
    word_cloud2 = WordCloud(width=1600, height=800,collocations = False, background_color = 'white').generate(string)
	# # Display the generated Word Cloud

    plt.imshow(word_cloud2)
    plt.axis("off")
    plt.show()


create_word_cloud(dataset)    
# word_cloud2 = WordCloud(collocations = False, background_color = 'white').generate(test3)
# # Display the generated Word Cloud

# plt.imshow(word_cloud2, interpolation='bilinear')
# plt.axis("off")
# plt.figure(figsize=(20,20))
# plt.show()

