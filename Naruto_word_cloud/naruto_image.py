# Create word cloud in specific shape

import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

dataset = open("clean_transcript.txt", "r", encoding="utf8").read()
def create_word_cloud(string):
    maskArray = npy.array(Image.open("naruto.jpg"))
    cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("naruto_cloud.png")
dataset = dataset.lower()
create_word_cloud(dataset)


# blend word cloud with original image

import cv2

bg = cv2.imread('naruto.jpg', cv2.IMREAD_COLOR)
fg = cv2.imread('naruto_cloud.png', cv2.IMREAD_COLOR)

blend = cv2.addWeighted(bg, 0.1, fg, 0.9, 0.0)
cv2.imwrite('blended.jpg', blend)