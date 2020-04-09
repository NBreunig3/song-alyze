# spotify.py
# This is where we will write our methods using spotipy to interact with the Spotify API
# LAST MODIFIED: 4/8/20

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
# tracks is a list of track id's
def create_playlist(tracks, name="Custom Playlist", public_playlist=False, description="Custom Playlist built by song-alyze"):
    playlist = sp.user_playlist_create(user=sp.current_user()["id"], name=name, public=public_playlist, description=description)
    sp.user_playlist_add_tracks(user=sp.current_user()["id"], playlist_id=playlist["id"], tracks=tracks)


# Function to create a playlist based on your top artists and songs
# name - the name of the playlist
# description - description of playlist
# public_playlist - boolean, true if public
# time_frame - the time frame (short_term, medium_term, long_term) to determine your top artists and tracks from
# limit - number of songs
# strictly_new - boolean, true if you want this playlist to contain songs that are NOT in your current library (playlists or user library)
#  Note: if you use strictly_new, function will be slower since it needs to scan through user's library
# TODO: Nathan - refactor so it doesn't add the a different version of the same song (compare title and artist)
def create_recommended_playlist(name="song-alyze Recommendations", description="Here's some tracks you might like!", public_playlist=False, time_frame="long_term", limit=50, strictly_new=False):
    artist_seeds = [artist["id"] for artist in get_top_artists(3, time_frame)]
    track_seeds = [track["id"] for track in get_top_tracks(2, time_frame)]
    tracks = get_recommended_tracks(artists_seeds=artist_seeds, track_seeds=track_seeds, limit=limit)
    if strictly_new:
        master_track_list = get_master_track_list()
        for track in tracks:
            if track["id"] in master_track_list:
                tracks.remove(track)
                #print("removed {}".format(track["name"]))
        while len(tracks) < limit:
            #print("ran new")
            new_tracks = get_recommended_tracks(artists_seeds=artist_seeds, track_seeds=track_seeds, limit=limit)
            for new_track in new_tracks:
                if (new_track["id"] not in master_track_list) and (new_track not in tracks) and (len(tracks) < limit):
                    #print("added new {}".format(new_track["name"]))
                    #print("{} not in master".format(new_track["name"])) if new_track["id"] not in master_track_list else print("{} in master".format(new_track["name"]))
                    tracks.append(new_track)
    create_playlist([track["id"] for track in tracks], name=name, description=description, public_playlist=public_playlist)


# A function that can get recommended artists, tracks, or genres
# Provide either a list of artists, tracks, or genres (id's)
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


# Function to get a set of all saved song id's in the user's library
# This includes songs from saved playlists and songs in library
# Returns a set! Not a list!
def get_master_track_list():
    master_track_list = set()
    # use set since we only want to know if a song is in the set. Gets the benefit of hashing.
    # O(1) time complexity and no duplicates
    playlist_ids = [p["id"] for p in sp.current_user_playlists()["items"]]
    for p in playlist_ids:
        p_len = sp.playlist(p)["tracks"]["total"]
        current_offset = 0
        while current_offset <= p_len:
            for s in sp.playlist_tracks(p, limit=100, offset=current_offset)["items"]:
                master_track_list.add(s["track"]["id"])
            current_offset += 100
    for item in sp.current_user_saved_tracks()["items"]:
        master_track_list.add(item["track"]["id"])
    return master_track_list


# Function to check if a song is already saved in the currently user's library,
# useful for checking to see if a user likes/has heard a song before
# songs is a list of one or more song ids
# Returns list of dictionary's with song name, id, and boolean true or false indicating if the song is saved in the user's library
def in_library(songs):
    saved_or_not = sp.current_user_saved_tracks_contains(songs)
    out = []
    for i in range(len(songs)):
        out.append({"name": sp.track(songs[i])["name"], "id": songs[i], "in_lib": saved_or_not[i]})
    return out


# Function to check if a single song is in a users saved library
# Returns a boolean
def song_in_library(song):
    return in_library(song)[0]["in_lib"]
