# wordcloud.py
# This file contains all functions dealing with the wordcloud API
# LAST MODIFIED: 4/7/20

from wordcloud import WordCloud # Documentation for word_cloud: https://amueller.github.io/word_cloud/references.html
import matplotlib.pyplot as plot  # matplotlib


def generate(text):
    wc = WordCloud(width=1920, height=1080, prefer_horizontal=0.6, background_color="white", font_path="../res/fonts/Marvind.ttf").generate(text)
    plot.figure(figsize=(20, 10))
    plot.imshow(wc, interpolation="bilinear")
    plot.axis("off")
    plot.tight_layout(pad=0)
    plot.show()



