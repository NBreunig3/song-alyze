# song-alyze
# main.py
# Authors: Nathan Breunig, Kylei Hoffland, Giannia Lammer, Jon Noel
# LAST MODIFIED: 4/29/20

import spotify  # Local import of spotify.py
import tkinter  # GUI  Reference: https://www.tutorialspoint.com/python/python_gui_programming.htm
from tkinter import font as tkFont
from tkinter import messagebox
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
    center_in_screen(main_window)
    font = tkFont.Font(family="Segoe UI", size=11)
    main_window.option_add("*Font", font)
    btn_dim = {"w": 30, "h": 5}
    btn_pad = {"x": 5, "y": 5}
    top_btn = tkinter.Button(main_window, text="Top Tracks & Artists", width=btn_dim["w"], height=btn_dim["h"],
                                    command=lambda: show_dual_list_dialog("Top"))
    rec_btn = tkinter.Button(main_window, text="Recommended Tracks & Artists", width=btn_dim["w"], height=btn_dim["h"],
                                 command=lambda: show_dual_list_dialog("Rec"))
    gen_rec_playlist_btn = tkinter.Button(main_window, text="Generate Recommended Playlist", width=btn_dim["w"],
                                          height=btn_dim["h"])
    gen_wordcloud_btn = tkinter.Button(main_window, text="Generate Word Cloud", width=btn_dim["w"], height=btn_dim["h"],
                                       command=lambda : word_cloud_dialog())
    top_btn.grid(row=0, column=0, padx=btn_pad["x"], pady=btn_pad["y"])
    rec_btn.grid(row=0, column=1, padx=btn_pad["x"], pady=btn_pad["y"])
    gen_rec_playlist_btn.grid(row=1, column=0, padx=btn_pad["x"], pady=btn_pad["y"])
    gen_wordcloud_btn.grid(row=1, column=1, padx=btn_pad["x"], pady=btn_pad["y"])
    spotify.get_master_track_list()
    main_window.mainloop()


# Function that creates a new window with 2 list boxes
# Called by Top and Rec buttons
def show_dual_list_dialog(type):
    # Used as a pointer to point to the current list in this dialog
    # so that the create a playlist buttons knows which list to use
    cur_list = []

    # Function to handle the create playlist button
    def create_playlist_btn_click(list):
        spotify.create_playlist([list[i]["id"] for i in range(int(default_num_option.get()))], name="Your Top Tracks")
        messagebox.showinfo("Success", "Playlist Created!")

    def on_dropdown_change(*args):
        tf = default_timeframe_option.get().lower().split(" ")
        tf = "_".join(tf)
        try:
            get_content(time_frame=tf, limit=int(default_num_option.get()))
        except NameError:
            get_content(time_frame=tf)

    def disp_listbox(order, list, number, include_artist, limit):
        lb = tkinter.Listbox(listbox_frame, width=50, height=25, selectmode=tkinter.BROWSE)
        index = 1
        for i in range(0, min(len(list), limit)):
            if number:
                if include_artist:
                    lb.insert(index, "{}.  {}  -  {}".format(index, list[i]["name"], list[i]["artist"]))
                else:
                    lb.insert(index, "{}.  {}".format(index, list[i]["name"]))
            else:
                if include_artist:
                    lb.insert(index, "{}  -  {}".format(list[i]["name"], list[i]["artist"]))
                else:
                    lb.insert(index, "{}".format(list[i]["name"]))
            index += 1
        lb.grid(row=0, column=order, padx=5, pady=5)

    def get_content(time_frame="long_term", limit=50):
        if type == "Top":
            # Top Tracks stuff
            top_tracks = spotify.get_top_tracks(50, time_range=time_frame) if not "tt-" + time_frame in cache else cache["tt-" + time_frame]
            cache["tt-" + time_frame] = top_tracks
            cache["cur"] = cache["tt-" + time_frame]
            disp_listbox(0, top_tracks, True, True, limit)
            # Top Artists stuff
            top_artists = spotify.get_top_artists(50, time_range=time_frame) if not "ta-" + time_frame in cache else cache[
                "ta-" + time_frame]
            cache["ta-" + time_frame] = top_artists
            disp_listbox(1, top_artists, True, False, limit)
        elif type == "Rec":
            # Rec Tracks stuff
            rec_tracks = spotify.get_recommended_tracks(limit=50) if not "rt" in cache else cache["rt"]
            cache["rt"] = rec_tracks
            cache["cur"] = cache["rt"]
            disp_listbox(0, rec_tracks, False, True, limit)
            # Rec Artists stuff
            rec_artists = spotify.get_recommended_artists(time_range=time_frame, limit=50) if not "ra-" + time_frame in cache else \
            cache["ra-" + time_frame]
            cache["ra-" + time_frame] = rec_artists
            disp_listbox(1, rec_artists, False, False, limit)
        else:
            print("Unsupported option passed into the show_list function.")
            exit()

    top = tkinter.Toplevel()
    top.grab_set()
    option_frame = tkinter.Frame(top)
    option_frame.grid(row=0)
    listbox_frame = tkinter.Frame(top)
    listbox_frame.grid(row=1)
    top.title(type)
    top.resizable(False, False)

    # option frame widgets
    gen_playlist_btn = tkinter.Button(option_frame, text="Create Playlist", width=15, height=1,
                                      command=lambda: create_playlist_btn_click(cache["cur"]))
    gen_playlist_btn.grid(row=0, column=0, padx=5, pady=5)
    time_frame_options = ["Short Term", "Medium Term", "Long Term"]
    default_timeframe_option = tkinter.StringVar(option_frame)
    default_timeframe_option.trace("w", on_dropdown_change)
    default_timeframe_option.set(time_frame_options[2])
    time_frame_menu = tkinter.OptionMenu(option_frame, default_timeframe_option, *time_frame_options)
    time_frame_menu.grid(row=0, column=1, padx=5, pady=5)
    number_options = [10, 25, 50]
    default_num_option = tkinter.StringVar(option_frame)
    default_num_option.trace("w", on_dropdown_change)
    default_num_option.set(number_options[2])
    number_menu = tkinter.OptionMenu(option_frame, default_num_option, *number_options)
    number_menu.grid(row=0, column=2, padx=5, pady=5)

    center_in_screen(top)
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


# this shit broken
# I no good at maths, maybe someone cold figure it out lol
# I no use GUI, GUI is the devil
def center_in_screen(window):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width / 2) - (window.winfo_reqwidth()+50)
        y = screen_height / 2 - (window.winfo_reqheight())
        window.geometry("+%d+%d" % (x, y))


if __name__ == "__main__":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # solves blurry tkinter widgets...thanks stack overflow
    main()
