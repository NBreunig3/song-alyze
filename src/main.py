# song-alyze
# main.py
# Authors: Nathan Breunig, Kylei Hoffland, Giannia Lammer, Jon Noel
# LAST MODIFIED: 3/27/20

import spotify  # Local import of spotify.py


def main():
    top_tracks = spotify.get_top_tracks(limit=10, time_range="short_term")
    top_artists = spotify.get_top_artists(limit=10, time_range="short_term")

    for i in range(len(top_tracks)):
        print("{}. {}".format(i+1, top_tracks[i]["name"]))
    print("")
    for i in range(len(top_artists)):
        print("{}. {}".format(i+1, top_artists[i]["name"]))


if __name__ == "__main__":
    main()
