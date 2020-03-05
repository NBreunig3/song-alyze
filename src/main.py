import spotipy  # Documentation for spotipy: https://spotipy.readthedocs.io/en/2.9.0/
import config   # config.py file that holds API id's for Spotify
# TODO: Rewrite the above import statements so that "main.py" can be called from the command line without errors of
#  missing modules
# song-alyze
# Authors: Nathan Breunig, Kylei Hoffland, Giannia Lammer, Jon Noel
# LAST MODIFIED: 3/4/20

# Example on how to prompt Spotify user for authorization access to this program
# TODO: See if pasting URL works in command line. Currently does not work in pycharm since ide console recognizes the
#  link
auth_token = spotipy.prompt_for_user_token(username="", scope="user-top-read", client_id=config.spotify_ids["client_id"], client_secret=config.spotify_ids["client_secret"], redirect_uri="http://localhost/")

sp = spotipy.Spotify(auth=auth_token)
print(sp.current_user_top_tracks())