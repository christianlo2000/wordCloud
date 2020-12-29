# script: wordCloud02.py
# genera nube de palabras
# funciona ok!
from os import path
#from scipy.misc import imread
import matplotlib.pyplot as plt
import random

from wordcloud import WordCloud, STOPWORDS

text = 'all your base are belong to us all of your base base base'
wordcloud = WordCloud(font_path='/Library/Fonts/Verdana.ttf',
                         relative_scaling = 1.0,
                         stopwords = {'to', 'of'} # set or space-separated string
                         ).generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
print("Nueva version 2")
