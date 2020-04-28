import lyricsgenius
import config

from word_cloud_gen import make_cloud, get_frequency_dict_for_text

# authorizes user using client id that is stored in config
genius = lyricsgenius.Genius(config.genius_ids['client_id'])


# test method to pass in lyrics from a genius URL, scrape it for punctuation
# then, this method generates the word cloud by first calculating the frequency of words
# used in the lyrics (Using multi dictionary)
def word_cloud_generator():
    song_lyrics = genius._clean_str(genius._scrape_song_lyrics_from_url("https://genius.com/The-scotts-travis-scott-and-kid-cudi-the-scotts-lyrics"))
    make_cloud(get_frequency_dict_for_text(song_lyrics))
    print(get_frequency_dict_for_text(song_lyrics))
