# wordcloud.py
# This file contains all functions dealing with the wordcloud API
# LAST MODIFIED: 5/1/20

from wordcloud import WordCloud # Documentation for word_cloud: https://amueller.github.io/word_cloud/references.html
import matplotlib.pyplot as plot  # matplotlib
import random


# Function to generate a word cloud
# text is a space separated string of words

def generate(text, prefer_horizontal=0.6, back_color="black", font_path="../res/fonts/Marvind.ttf"):
    # generates a random color for the background
    if back_color == "random":
        back_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    #creates word cloud    
    wc = WordCloud(width=1920, height=1080, prefer_horizontal=prefer_horizontal, background_color=back_color, font_path=font_path).generate_from_frequencies(text)
    plot.figure(figsize=(20, 10))
    plot.imshow(wc, interpolation="bilinear")
    plot.axis("off")
    plot.tight_layout(pad=0)
    plot.show()
