# song-alyze
# main.py
# Authors: Nathan Breunig, Kylei Hoffland, Giannia Lammer, Jon Noel
# LAST MODIFIED: 4/27/20

import spotify  # Local import of spotify.py
import tkinter  # GUI  Reference: https://www.tutorialspoint.com/python/python_gui_programming.htm
import genius  # Local import of genius.py

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
    top_art_btn = tkinter.Button(main_window, text="Top Artists", width=btn_dim["w"], height=btn_dim["h"],
                                 command=lambda: show_list("Top Artists"))
    rec_art_btn = tkinter.Button(main_window, text="Recommended Artists", width=btn_dim["w"], height=btn_dim["h"],
                                 command=lambda: show_list("Rec Artists"))
    rec_tracks_btn = tkinter.Button(main_window, text="Recommended Tracks", width=btn_dim["w"], height=btn_dim["h"],
                                    command=lambda: show_list("Rec Tracks"))
    gen_rec_playlist_btn = tkinter.Button(main_window, text="Generate Recommended Playlist", width=btn_dim["w"],
                                          height=btn_dim["h"])
    gen_wordcloud_btn = tkinter.Button(main_window, text="Generate Word Cloud", width=btn_dim["w"], height=btn_dim["h"],
                                       command=lambda : word_cloud_dialog())
    top_art_btn.grid(row=0, column=0, padx=btn_pad["x"], pady=btn_pad["y"])
    top_tracks_btn.grid(row=1, column=0, padx=btn_pad["x"], pady=btn_pad["y"])
    rec_art_btn.grid(row=0, column=1, padx=btn_pad["x"], pady=btn_pad["y"])
    rec_tracks_btn.grid(row=1, column=1, padx=btn_pad["x"], pady=btn_pad["y"])
    gen_rec_playlist_btn.grid(row=0, column=2, padx=btn_pad["x"], pady=btn_pad["y"])
    gen_wordcloud_btn.grid(row=1, column=2, padx=btn_pad["x"], pady=btn_pad["y"])
    # make_cloud(get_frequency_dict_for_text(text));
    main_window.mainloop()


# Function to create a new window with a listbox
# Should be called by top tracks, top artists, rec artists, rec tracks buttons
# TODO: Add the ability to customize the API call as another menu item.
#   i.e an option to change the time range and number of items to get
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
    else:
        print("Unsupported option passed into the show_list function.")
        exit()
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


# TODO
# Function should display a pop up window to select the method of word cloud generation
#   Possible Options are: top artists, top tracks, top lyrics, etc
# This function will be called by the "Generate Word Cloud" button
def word_cloud_dialog():
    # TODO
    genius.gen_word_freq_word_cloud()
    print()


# Nathan TODO
def gen_rec_playlist_dialog():
    print()


if __name__ == "__main__":
    main()
