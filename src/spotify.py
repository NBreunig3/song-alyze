# spotify.py
# This is where we will write our methods using spotipy to interact with the Spotify API
# LAST MODIFIED: 3/27/20

import spotipy  # Documentation for spotipy: https://spotipy.readthedocs.io/en/2.9.0/
import config  # Spotify API id's

# Various scopes to get access to. View scopes here: https://developer.spotify.com/documentation/general/guides/scopes/
__SPOTIFY_SCOPES__ = "user-top-read playlist-read-private user-read-recently-played playlist-modify-private playlist-modify-public"  # Should not be changed after this line
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
    sp.user_playlist_add_tracks(user=sp.current_user()["id"] , playlist_id=playlist["id"], tracks=track_ids)
