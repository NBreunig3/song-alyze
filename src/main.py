# song-alyze
# main.py
# Authors: Nathan Breunig, Kylei Hoffland, Giannia Lammer, Jon Noel
# LAST MODIFIED: 4/23/20

import tkinter  # GUI  Reference: https://www.tutorialspoint.com/python/python_gui_programming.htm

from genius import word_cloud_generator
from word_cloud_gen import *
# To make sure Python recognizes our libraries
import spotify  # Local import of spotify.py

cache = {}  # Used to cache the results of API calls in main.py. USE THIS! See the "show_list" function as example.

# As of 4/23/20 currently implementing GUI
# TODO:
# Change theme of overall application. (4/23/20 - Tried and wasn't working)
# Map the rest of buttons to functions
#   - top tracks, top artists, rec tracks, can all use the show_list function below
#     See top_tracks as an example
# Add the ability to customize the calls in the GUI (i.e. changing time_range and other function parameters)
# Make pop up windows "focused" (i.e. can't go back to previously windows while current one is opened)
# Make windows show in the center of screen


def main():
    # Beginning of GUI
    main_window = tkinter.Tk(screenName="song-alyze", )
    main_window.title("song-alyze")
    main_window.resizable(False, False)
    btn_dim = {"w": 25, "h": 5}
    btn_pad = {"x": 5, "y": 5}
    top_tracks_btn = tkinter.Button(main_window, text="Top Tracks", width=btn_dim["w"], height=btn_dim["h"],
                                    command=lambda: show_list("Top Tracks"))
    top_art_btn = tkinter.Button(main_window, text="Top Artists", width=btn_dim["w"], height=btn_dim["h"])
    rec_art_btn = tkinter.Button(main_window, text="Recommended Artists", width=btn_dim["w"], height=btn_dim["h"])
    rec_tracks_btn = tkinter.Button(main_window, text="Recommended Tracks", width=btn_dim["w"], height=btn_dim["h"])
    gen_rec_playlist_btn = tkinter.Button(main_window, text="Generate Recommended Playlist", width=btn_dim["w"],
                                          height=btn_dim["h"])
    gen_wordcloud_btn = tkinter.Button(main_window, text="Generate Word Cloud", width=btn_dim["w"], height=btn_dim["h"],
                                       command=lambda : gen_wordcloud())
    top_art_btn.grid(row=0, column=0, padx=btn_pad["x"], pady=btn_pad["y"])
    top_tracks_btn.grid(row=1, column=0, padx=btn_pad["x"], pady=btn_pad["y"])
    rec_art_btn.grid(row=0, column=1, padx=btn_pad["x"], pady=btn_pad["y"])
    rec_tracks_btn.grid(row=1, column=1, padx=btn_pad["x"], pady=btn_pad["y"])
    gen_rec_playlist_btn.grid(row=0, column=2, padx=btn_pad["x"], pady=btn_pad["y"])
    gen_wordcloud_btn.grid(row=1, column=2, padx=btn_pad["x"], pady=btn_pad["y"])
    # make_cloud(get_frequency_dict_for_text(text));
    main_window.mainloop()


def show_list(type):
    top = tkinter.Toplevel()
    top.title(type)
    top.resizable(False, False)
    list = []
    if type == "Top Tracks":
        list = spotify.get_top_tracks(50) if not "tt" in cache else cache["tt"]
        cache["tt"] = list
    elif type == "Top Artists":
        list = spotify.get_top_artists(50) if not "ta" in cache else cache["ta"]
        cache["ta"] = list
    menu = tkinter.Menu(top)
    menu.add_command(label="Create Playlist", command=lambda: spotify.create_playlist([x["id"] for x in list],
                                                                                      "Your" + type))
    top.config(menu=menu)
    lb = tkinter.Listbox(top, width=50, height=25, selectmode=tkinter.BROWSE)
    index = 1
    for x in list:
        lb.insert(index, "{}.  {}".format(index, x["name"]))
        index += 1
    lb.pack()
    top.mainloop()


# method used when "Generate Wordcloud" button is pressed
# Still need to decided which lyrics to pass in (current song or the lyrics from all top ten?)
def gen_wordcloud():
    word_cloud_generator()


if __name__ == "__main__":
    main()
