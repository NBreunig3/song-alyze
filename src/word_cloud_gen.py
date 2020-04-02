# wordcloud.py
# This file contains all functions dealing with the wordcloud API
# LAST MODIFIED: 4/2/20

import wordcloud  # Documentation for word_cloud: https://github.com/amueller/word_cloud
import matplotlib.pyplot as plot  # matplotlib


def generate(text):
    wc = wordcloud.WordCloud().generate(text)
    plot.imshow(wc, interpolation="bilinear")
    plot.axis("off")
    plot.show()



