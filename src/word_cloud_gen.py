# wordcloud.py
# This file contains all functions dealing with the wordcloud API
# LAST MODIFIED: 4/30/20

from wordcloud import WordCloud # Documentation for word_cloud: https://amueller.github.io/word_cloud/references.html
import matplotlib.pyplot as plot  # matplotlib


# Function to generate a word cloud
# text is a space separated string of words
def generate(text, prefer_horizontal=0.6, back_color="white", font="../res/fonts/Marvind.ttf"):
    wc = WordCloud(width=1920, height=1080, prefer_horizontal=prefer_horizontal, background_color=back_color, font_path=font).generate(text)
    plot.figure(figsize=(20, 10))
    plot.imshow(wc, interpolation="bilinear")
    plot.axis("off")
    plot.tight_layout(pad=0)
    plot.show()
