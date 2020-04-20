# song-alyze
# main.py
# Authors: Nathan Breunig, Kylei Hoffland, Giannia Lammer, Jon Noel
# LAST MODIFIED: 4/20/20

# To make sure Python recognizes our libraries
import spotify  # Local import of spotify.py
import word_cloud_gen  # Local import of word_cloud_gen.py
import tkinter  # GUI


def main():
    # Beginning of GUI
    # main_window = tkinter.Tk(screenName="song-alyze")
    # main_window.title("song-alyze")
    # btn_dim = {"w": 25, "h": 5}
    # btn_pad = {"x": 5, "y": 5}
    # top_tracks_btn = tkinter.Button(main_window, text="Top Tracks", width=btn_dim["w"], height=btn_dim["h"])
    # top_art_btn = tkinter.Button(main_window, text="Top Artists", width=btn_dim["w"], height=btn_dim["h"])
    # rec_art_btn = tkinter.Button(main_window, text="Recommended Artists", width=btn_dim["w"], height=btn_dim["h"])
    # rec_tracks_btn = tkinter.Button(main_window, text="Recommended Tracks", width=btn_dim["w"], height=btn_dim["h"])
    # gen_rec_playlist_btn = tkinter.Button(main_window, text="Generate Recommended Playlist", width=btn_dim["w"], height=btn_dim["h"])
    # gen_wordcloud_btn = tkinter.Button(main_window, text="Generate Word Cloud", width=btn_dim["w"], height=btn_dim["h"])
    # top_art_btn.grid(row=0, column=0, padx=btn_pad["x"], pady=btn_pad["y"])
    # top_tracks_btn.grid(row=1, column=0, padx=btn_pad["x"], pady=btn_pad["y"])
    # rec_art_btn.grid(row=0, column=1, padx=btn_pad["x"], pady=btn_pad["y"])
    # rec_tracks_btn.grid(row=1, column=1, padx=btn_pad["x"], pady=btn_pad["y"])
    # gen_rec_playlist_btn.grid(row=0, column=2, padx=btn_pad["x"], pady=btn_pad["y"])
    # gen_wordcloud_btn.grid(row=1, column=2, padx=btn_pad["x"], pady=btn_pad["y"])
    # main_window.mainloop()


    top_tracks = spotify.get_top_tracks(limit=10, time_range="short_term")
    top_artists = spotify.get_top_artists(limit=10, time_range="short_term")
    recommended_artists = spotify.get_recommended_artists(time_range="short_term")
    in_library = spotify.in_library([s["id"] for s in top_tracks])
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

    print("\nRecommended Tracks")  # Recommended Tracks
    for track in rec_tracks:
        print("  \"{}\" by {}".format(track["name"], track["artist"]))

    # In library checker
    print("\nIs {} (your top track) saved in your library?".format(top_tracks[0]["name"]))
    print(in_library[0]["in_lib"])

    # Make a wordcloud based on your top artists
    word_cloud_gen.generate(" ".join([a["name"].replace(" ", "") for a in top_artists]))

    # Create a recommended playlist. All songs that are not currently in user library
    # Uncomment if you want the playlist created
    # spotify.create_recommended_playlist(strictly_new=True)


if __name__ == "__main__":
    main()
