# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:33:55 2021

@author: Chad.Daud
"""
'''
For this to work correctly, please install the following:
matplotlib -- run the folllowing: pip install matplotlib
wordcloud -- pip install wordcloud
'''

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 
# stopwords is a collection of words that dont convey meaning. mostly pronouns such as he she etc.

#generate word cloud

text = input("Add your content here: ")
#generate the wordcloud object, set the height and width, set the random_state parameter to ensure
#reproducibility of results and set the stopwords parameter so that the irrelevant words such as pronouns are discarded.
wordcloud = WordCloud(width = 5000, height = 3000, random_state=1, background_color='red', collocations=False, stopwords = STOPWORDS).generate(text)
# text is the input to the generate() method
#draw the figure
#Set figure size
plt.figure(figsize=(40, 30))
# Display image
plt.imshow(wordcloud) 
# No axis 
plt.axis("off")
plt.show()
