# song-alyze
# main.py
# Authors: Nathan Breunig, Kylei Hoffland, Giannia Lammer, Jon Noel
# LAST MODIFIED: 4/2/20

# To make sure Python recognizes our libraries
import sys
sys.path.append("../libs/spotipy/")
import spotify  # Local import of spotify.py


def main():
    top_tracks = spotify.get_top_tracks(limit=10, time_range="short_term")
    top_artists = spotify.get_top_artists(limit=10, time_range="short_term")
    recommended_artists = spotify.get_recommended_artists(time_range="short_term")
    in_library = spotify.in_library([top_tracks[0]["id"]])
    rec_tracks = spotify.get_recommended_tracks(track_seeds=[x["id"] for x in top_tracks][:5], limit=10)

    print("Top Tracks")  # Top Tracks
    for i in range(len(top_tracks)):
        print("{}. {}".format(i+1, top_tracks[i]["name"]))

    print("\nTop Artists")  # Top Artists
    for i in range(len(top_artists)):
        print("{}. {}".format(i+1, top_artists[i]["name"]))

    print("\nRecommended Artists")  # Recommended Artists
    for i in range(len(recommended_artists)):
        print("{}. {}".format(i+1, recommended_artists[i]["name"]))

    # In library checker
    print("\nIs {} (your top track) saved in your library?".format(top_tracks[0]["name"]))
    print(in_library[0]["in_lib"])

    print("\nRecommended Tracks")  # Recommended Tracks
    for track in rec_tracks:
        print("  \"{}\" by {}".format(track["name"], track["artist"]))


if __name__ == "__main__":
    main()
