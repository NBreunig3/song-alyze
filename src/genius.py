# genius.py
# Uses the genius API to get lyrics of songs
# LAST MODIFIED: 4/27/20

import lyricsgenius
import config
import word_cloud_gen as wc
import requests

# authorizes user using client id that is stored in config
genius = lyricsgenius.Genius(config.genius_ids['client_id'])


# test method to pass in lyrics from a genius URL, scrape it for punctuation
# then, this method generates the word cloud by first calculating the frequency of words
# used in the lyrics (Using multi dictionary)
# Function should eventually take in song id parameter
def gen_word_freq_word_cloud(song_lyrics_url):
    song_lyrics = genius._clean_str(genius._scrape_song_lyrics_from_url(song_lyrics_url))
    dict = word_freqs(song_lyrics)
    # sort dict
    sort = sorted(dict, key=lambda x: dict[x], reverse=True)
    # keeps only the top 175 words from list
    sort = sort[:175]
    # generate word cloud
    wc.generate(" ".join(sort))


# Function to count the word frequencies of a space separated string
# Returns a dictionary mapping a string to a integer frequency
def word_freqs(string):
    # Used to omit the follow words from word cloud generation
    __exclude_words__ = "a the an to in for of or by with is on this that be who where i im youre you are ill and "
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


# Function should search by the parameter song_name and artist_name and return the lyrics
def get_song_lyrics(song_name="Rap God", artist_name="Eminem"):
    base_url = "https://api.genius.com"
    headers = {'Authorization': 'Bearer 4VCfSDiSstA8ZzJd9Z5rFPNoODBR8XT13e_5uHeLOWqkmWzApPiNa-MYnYH_wOlq'}
    search_url = base_url + "/search"
    song_title = song_name
    artist_name = artist_name
    data = {'q': song_title}
    response = requests.get(search_url, data=data, headers=headers)
    json = response.json()
    song_info = None
    for hit in json["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == artist_name:
            song_info = hit
            break
    if song_info:
        pass
        song_lyrics_url = song_info['result']['url']  # returns the lyrics URL, used to scrape lyrics from
        return song_lyrics_url


# Function used to retrieve all lyrics from the passed in set and generate a word cloud
# set_of_artists_and_songs created in the get_master_track_list function of spotify
def get_bulk_song_lyrics(master_track_atts):
    song_title = []
    artist_name = []
    for x in master_track_atts:
        song_title.append(x.split("!")[0])
        artist_name.append(x.split("!")[1])
    list_of_urls = [get_song_lyrics(song_title[x], artist_name[x]) for x in range(len(song_title))]
    total_song_lyrics = ""
    for url in list_of_urls:
        if url is not None:
            total_song_lyrics += genius._clean_str(genius._scrape_song_lyrics_from_url(url))
    lyric_dict = word_freqs(total_song_lyrics)
    # sort dict
    sort = sorted(lyric_dict, key=lambda x: lyric_dict[x], reverse=True)
    # keeps only the top 175 words from list
    sort = sort[:175]
    # generate word cloud
    wc.generate(" ".join(sort))



