# wordcloud.py
# This file contains all functions dealing with the wordcloud API
# LAST MODIFIED: 4/8/20

from wordcloud import WordCloud # Documentation for word_cloud: https://amueller.github.io/word_cloud/references.html
import matplotlib.pyplot as plot  # matplotlib
import numpy as np
import multidict as multidict
import os
import re
from PIL import Image
from os import path

# Used to omit the follow words from word cloud generation
common_words_pattern = "a|the|an|to|in|for|of|or|by|with|is|on|this|that|be|who|where"

# Function to generate a word cloud
# text is a space separated string of words
def generate(text):
    wc = WordCloud(width=1920, height=1080, prefer_horizontal=0.6, background_color="white", font_path="../res/fonts/Marvind.ttf").generate(text)
    plot.figure(figsize=(20, 10))
    plot.imshow(wc, interpolation="bilinear")
    plot.axis("off")
    plot.tight_layout(pad=0)
    plot.show()


# sentence is a full line of text (lyrics), space separated
def get_frequency_dict_for_text(sentence):
    lyric_terms_dict = multidict.MultiDict()
    tmp_dict = {}

    # making dict for counting frequencies
    for text in sentence.split(" "):
        if re.match(common_words_pattern, text):
            continue
        val = tmp_dict.get(text, 0)
        tmp_dict[text.lower()] = val + 1
    for key in tmp_dict:
        lyric_terms_dict.add(key, tmp_dict[key])
    return lyric_terms_dict


def make_cloud(text):
    # limit wordcloud to 25 for testing purposes
    wc = WordCloud(width=1920, height=1080, prefer_horizontal=0.6, background_color="white", font_path="../res/fonts/Marvind.ttf", max_words=25)
    # generate word cloud using frequencies
    wc.generate_from_frequencies(text)

    # display the wordcloud
    plot.imshow(wc, interpolation="bilinear")
    plot.axis("off")
    plot.show()

