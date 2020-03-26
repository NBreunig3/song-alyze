import spotipy  # Documentation for spotipy: https://spotipy.readthedocs.io/en/2.9.0/
from . import config  # Spotify API id's

# Various scopes to get access to. View scopes here: https://developer.spotify.com/documentation/general/guides/scopes/
__SPOTIFY_SCOPES = "user-top-read playlist-read-private user-read-recently-played"  # Should not be changed after this line
# Authorization token specific to the users account
__AUTH_TOKEN = spotipy.prompt_for_user_token(username="", scope=__SPOTIFY_SCOPES, client_id=config.spotify_ids["client_id"],
                                           client_secret=config.spotify_ids["client_secret"],
                                           redirect_uri="http://localhost/")
#  If AUTH_TOKEN is legit...
if __AUTH_TOKEN:
    # Use sp to call Spotify API functions. List of API endpoints: https://developer.spotify.com/documentation/web-api/reference/
    global sp
    sp = spotipy.Spotify(auth=__AUTH_TOKEN)
else:
    print("Error with AUTH_TOKEN")
    exit()


# Function to get the users top tracks. Limit is the number of tracks to get,
# time_range is what period of time to use: short_term, medium_term, or long_term
def get_top_tracks(limit=10, time_range="long_term"):
    dict = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    top_list = list()
    for x in dict["items"]:
        top_list.append((x["name"], x["id"]))
    return top_list


# Function to get the users top artists. Limit is the number of tracks to get,
# # time_range is what period of time to use: short_term, medium_term, or long_term
def get_top_artists(limit=10, time_range="long_term"):
    dict = sp.current_user_top_artists(limit=limit, time_range=time_range)
    top_list = list()
    for x in dict["items"]:
        top_list.append((x["name"], x["id"]))
    return top_list