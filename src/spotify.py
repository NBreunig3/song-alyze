# spotify.py
# This is where we will write our methods using spotipy to interact with the Spotify API
# LAST MODIFIED: 4/2/20

import spotipy  # Documentation for spotipy: https://spotipy.readthedocs.io/en/2.9.0/
import config  # Spotify API id's

# Various scopes to get access to. View scopes here: https://developer.spotify.com/documentation/general/guides/scopes/
__SPOTIFY_SCOPES__ = "user-top-read playlist-read-private user-read-recently-played playlist-modify-private playlist-modify-public user-library-read"  # Should not be changed after this line
# Authorization token specific to the users account
__AUTH_TOKEN__ = spotipy.prompt_for_user_token(username="", scope=__SPOTIFY_SCOPES__, client_id=config.spotify_ids["client_id"],
                                           client_secret=config.spotify_ids["client_secret"],
                                           redirect_uri="http://localhost/")
#  If AUTH_TOKEN is legit...
if __AUTH_TOKEN__:
    # Use sp to call Spotify API functions. List of API endpoints: https://developer.spotify.com/documentation/web-api/reference/
    global sp
    sp = spotipy.Spotify(auth=__AUTH_TOKEN__)
else:
    print("Error with AUTH_TOKEN")
    exit()


# Function to get the users top tracks. Limit is the number of tracks to get,
# time_range is what period of time to use: short_term, medium_term, or long_term
# Returns a list of dictionaries
def get_top_tracks(limit=10, time_range="long_term"):
    dict = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    top_list = []  # list of dictionaries
    for x in dict["items"]:
        top_list.append({"name": x["name"], "id": x["id"], "type": x["type"], "popularity": x["popularity"]})
    return top_list


# Function to get the users top artists. Limit is the number of tracks to get,
# # time_range is what period of time to use: short_term, medium_term, or long_term
# Returns a list of dictionaries
def get_top_artists(limit=10, time_range="long_term"):
    dict = sp.current_user_top_artists(limit=limit, time_range=time_range)
    top_list = []  # list of dictionaries
    for x in dict["items"]:
        top_list.append({"name": x["name"], "id": x["id"], "type": x["type"], "popularity": x["popularity"]})
    return top_list


# Function to create a playlist based on a list of songs
# (IMPORTANT: list is a list of dictionaries with info about each song)
def create_playlist(list, name="Custom Playlist", public_playlist=False, collaboritive_playlist=False, description="Custom Playlist built by song-alyze"):
    playlist = sp.user_playlist_create(user=sp.current_user()["id"], name=name, public=public_playlist, description=description)
    track_ids = [track["id"] for track in list]  # Did I win the admiration of my peers lol
    sp.user_playlist_add_tracks(user=sp.current_user()["id"], playlist_id=playlist["id"], tracks=track_ids)


# A function that can get recommended artists, tracks, or genres
# Provide either a list of artists, tracks, or genres
# (NO MORE THAN 5 i.e. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres)
# Returns a list of dictionaries
def get_recommended_tracks(artists_seeds=None, track_seeds=None, genre_seeds=None, limit=10, country=None):
    rec = sp.recommendations(seed_artists=artists_seeds, seed_tracks=track_seeds, seed_genres=genre_seeds, limit=limit, country=country)
    rec_list = []
    for track in rec["tracks"]:
        rec_list.append({"name": track["name"], "artist": track["artists"][0]["name"], "id": track["id"]})
    return rec_list


# Function to get recommended artists based on user's top artist.
# time_range is the period to get the top artist from--short_term, medium_term, or long_term
# Returns a list of dictionaries
def get_recommended_artists(time_range="long_term", limit=10):
    top = get_top_artists(limit=1, time_range=time_range)[0]["id"]
    recommend = sp.artist_related_artists(top)
    new_artists = []
    for r in recommend['artists']:
        new_artists.append({"name": r["name"], "id": r["id"], "type": r["type"], "popularity": r["popularity"]})
    return new_artists[:limit]


# Function to check if a song is already saved in the currently user's library,
# useful for checking to see if a user likes/has heard a song before
# songs is a list of one or more song ids
# Returns list of dictions with song name, id, and boolean true or false indicating if the song is saved in the user's library
def in_library(songs):
    saved_or_not = sp.current_user_saved_tracks_contains(songs)
    out = []
    for i in range(len(songs)):
        out.append({"name": sp.track(songs[i]), "id": songs[i], "in_lib": saved_or_not[i]})
    return out
