# genius.py
# Uses the genius API to get lyrics of songs
# LAST MODIFIED: 5/2/20

import lyricsgenius
import config
import requests
import spotify
from cache import cache

# authorizes user using client id that is stored in config
print("Connecting to Genius Lyrics...")
genius = lyricsgenius.Genius(config.genius_ids['client_id'])
print("Connected to Genius")


def get_song_lyric_freq(song_name, song_artist):
    url = get_lyrics_url(song_name=song_name, song_artist=song_artist)
    if url is not None:
        song_lyrics = genius._clean_str(genius._scrape_song_lyrics_from_url(url))
        print(song_lyrics)
        return word_freqs(song_lyrics)


def get_top_song_lyric_freq(time_range="long_term", limit=10):
    top_tracks = cache["tt-"+time_range] if "tt-"+time_range in cache else spotify.get_top_tracks(time_range=time_range, limit=limit)
    urls = [get_lyrics_url(t["name"], t["artist"]) for t in top_tracks]
    lyrics = ""
    for url in urls:
        if url is not None:
            lyrics += genius._clean_str(genius._scrape_song_lyrics_from_url(url))
            lyrics += " "
            print(lyrics)
    return word_freqs(lyrics)


# Function to count the word frequencies of a space separated string
# Returns a dictionary mapping a string to a integer frequency
def word_freqs(string):
    # Used to omit the follow words from word cloud generation
    __exclude_words__ = "a the an to in for of or by with is on this that be who where i im youre you are ill and "
    common_words = set(x for x in __exclude_words__.split(" "))
    punc = ",./?!()-\"\';"
    dict = {}

    string = string.replace("\n", " ")
    to_del = []
    for i in range(len(string)):
        if not string[i].isalnum() and string[i] != " ":
            to_del.append(i)
    new_str = ""
    for i in range(len(string)):
        if i not in to_del:
            new_str += string[i]

    string = new_str
    string = string.replace("chorus", "")
    string = string.replace("verse", "")
    for i in range(5):
        string = string.replace("verse {}".format(i), "")
    string = string.replace("bridge", "")
    words = string.lower().split(" ")

    # remove special chars and count words
    for word in words:
        if word not in common_words:
            if word[len(word)-1] == "s":
                word = word[:len(word)-1]
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
    return dict


# Function should search by the parameter song_name and artist_name and return the lyrics
def get_lyrics_url(song_name="Rap God", song_artist="Eminem"):
    base_url = "https://api.genius.com"
    headers = {'Authorization': 'Bearer 4VCfSDiSstA8ZzJd9Z5rFPNoODBR8XT13e_5uHeLOWqkmWzApPiNa-MYnYH_wOlq'}
    search_url = base_url + "/search"
    data = {'q': song_name}
    response = requests.get(search_url, data=data, headers=headers)
    json = response.json()
    song_info = None
    for hit in json["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == song_artist:
            song_info = hit
            break
    if song_info:
        pass
        song_lyrics_url = song_info['result']['url']  # returns the lyrics URL, used to scrape lyrics from
        return song_lyrics_url


# Function used to retrieve all lyrics from the passed in set and generate a word cloud
# set_of_artists_and_songs created in the get_master_track_list function of spotify
def get_bulk_lyric_freq():
    master_track_atts = spotify.get_master_track_list()[1]
    master_word_dict = {}
    song_title = []
    artist_name = []
    for x in master_track_atts:
        song_title.append(x[x.find("<")+1:x.find(">")])
        x = x[x.find(">")+1:]
        artist_name.append(x[x.find("<")+1:x.find(">")])
    list_of_urls = [get_lyrics_url(song_title[x], artist_name[x]) for x in range(len(song_title))]
    for url in list_of_urls:
        if url is not None:
            song_lyrics = genius._clean_str(genius._scrape_song_lyrics_from_url(url))
            lyric_list = song_lyrics.split(" ")
            for lyric in lyric_list:
                if lyric in master_word_dict:
                    master_word_dict[lyric] = master_word_dict[lyric] + 1
                else:
                    master_word_dict[lyric] = 1
    return master_word_dict



