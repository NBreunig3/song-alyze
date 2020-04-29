# genius.py
# Uses the genius API to get lyrics of songs
# LAST MODIFIED: 4/27/20

import lyricsgenius
import config
import word_cloud_gen as wc

# authorizes user using client id that is stored in config
genius = lyricsgenius.Genius(config.genius_ids['client_id'])


# test method to pass in lyrics from a genius URL, scrape it for punctuation
# then, this method generates the word cloud by first calculating the frequency of words
# used in the lyrics (Using multi dictionary)
# Function should eventually take in song id parameter
def gen_word_freq_word_cloud():
    song_lyrics = genius._clean_str(genius._scrape_song_lyrics_from_url("https://genius.com/The-scotts-travis-scott-and-kid-cudi-the-scotts-lyrics"))
    dict = word_freqs(song_lyrics)
    # sort dict
    sort = sorted(dict, key=lambda x: dict[x], reverse=True)
    # generate word cloud
    wc.generate(" ".join(sort))


# Function to count the word frequnecies of a space seperated string
# Returns a dictionary mapping a string to a integer frequency
def word_freqs(string):
    # Used to omit the follow words from word cloud generation
    __exclude_words__ = "a the an to in for of or by with is on this that be who where"
    common_words = set(x for x in __exclude_words__.split(" "))
    punc = ",./?!()-\"\';"
    dict = {}
    words = string.lower().split(" ")

    # remove special chars and count words
    for word in words:
        for p in punc:
            if p in word:
                word = word.replace(p, "")
        if word not in common_words:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
    return dict


# TODO
# Function should search by the parameter song_name and return the lyrics
def get_song_lyrics(song_name):
    print()
