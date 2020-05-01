# song-alyze
# main.py
# Authors: Nathan Breunig, Kylei Hoffland, Giannia Lammer, Jon Noel
# LAST MODIFIED: 4/30/20

import spotify  # Local import of spotify.py
import tkinter  # GUI  Reference: https://www.tutorialspoint.com/python/python_gui_programming.htm
from tkinter import font as tkFont
from tkinter import messagebox
import ttkthemes
import genius  # Local import of genius.py
import word_cloud_gen # Local import of word_cloud_gen.py
from tkinter import filedialog as fd
import os

cache = {}  # Used to cache the results of API calls in main.py. USE THIS! See the "show_list" function as example.

# Overall TODO:
# Change theme of overall application. (4/30/20 - Tried and wasn't working)
# Finish the word_cloud_dialog function (see comments on that function for details)


def main():
    # Beginning of GUI
    main_window = tkinter.Tk(screenName="song-alyze")
    main_window.title("song-alyze")
    main_window.resizable(False, False)
    theme = ttkthemes.ThemedStyle(main_window)
    theme.theme_use("arc")  # not working (4/30_
    info_frame = tkinter.Frame(main_window)
    content_frame = tkinter.Frame(main_window)
    info_frame.grid(row=0, column=0)
    content_frame.grid(row=1, column=0)
    center_in_screen(main_window)
    font = tkFont.Font(family="Segoe UI", size=11)
    main_window.option_add("*Font", font)
    btn_dim = {"w": 30, "h": 5}
    btn_pad = {"x": 10, "y": 10}

    wel_lbl_txt = tkinter.StringVar()
    wel_lbl_txt.set("Welcome {}".format(spotify.sp.current_user()["display_name"]))
    wel_lbl = tkinter.Label(info_frame, textvariable=wel_lbl_txt)
    tit_lbl_txt = tkinter.StringVar()
    tit_lbl_txt.set("song-alyze")
    title_lbl = tkinter.Label(info_frame, textvariable=tit_lbl_txt, font=("Segoe UI Bold", 14))
    top_btn = tkinter.Button(content_frame, text="Top Tracks & Artists", width=btn_dim["w"], height=btn_dim["h"],
                                    command=lambda: show_dual_list_dialog("Top"))
    rec_btn = tkinter.Button(content_frame, text="Recommended Tracks & Artists", width=btn_dim["w"], height=btn_dim["h"],
                                 command=lambda: show_dual_list_dialog("Rec"))
    gen_rec_playlist_btn = tkinter.Button(content_frame, text="Generate Recommended Playlist", width=btn_dim["w"],
                                          height=btn_dim["h"])
    gen_wordcloud_btn = tkinter.Button(content_frame, text="Generate Word Cloud", width=btn_dim["w"], height=btn_dim["h"],
                                       command=lambda: word_cloud_dialog())
    title_lbl.grid(row=0, column=0)
    wel_lbl.grid(row=1, column=0)
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
            top_tracks = spotify.get_top_tracks(limit=50, time_range=time_frame) if not "tt-" + time_frame in cache else cache["tt-" + time_frame]
            cache["tt-" + time_frame] = top_tracks
            cache["cur"] = cache["tt-" + time_frame]
            disp_listbox(0, top_tracks, True, True, limit)
            # Top Artists stuff
            top_artists = spotify.get_top_artists(limit=50, time_range=time_frame) if not "ta-" + time_frame in cache else cache[
                "ta-" + time_frame]
            cache["ta-" + time_frame] = top_artists
            disp_listbox(1, top_artists, True, False, limit)
        elif type == "Rec":
            # Rec Tracks stuff
            top_tracks = spotify.get_top_tracks(limit=50, time_range=time_frame) if not "tt-" + time_frame in cache else \
            cache["tt-" + time_frame]
            rec_tracks = spotify.get_recommended_tracks(limit=50, track_seeds=[x["id"] for x in top_tracks[:5]]) if not "rt-" + time_frame in cache else cache["rt-" + time_frame]
            cache["rt-" + time_frame] = rec_tracks
            cache["cur"] = cache["rt-" + time_frame]
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
    top.title(type + " Artists & Tracks")
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
# Function should display an options pop up window to select the method of word cloud generation
# Options should be:
#   - Data for the wordcloud (top tracks, top artists, lyrics?) (drop down menu)
#   - Wordcloud font to use (if left blank our font will be used)
#                           (allow the user the select his own from their local machine)
#                           (drop down dialog with the two fonts for res/ AND an option to open a custom font)
#   - prefer_horizontal paramter (see world_cloud_gen.py) (make this a slider from 0.0 to 1.0)
#   - background color
#   - any other options you can think of
#   A button called generate should be at the button of the winow. Will take all the parameters
#   from above into account and generate the respective word cloud
# This function will be called by the "Generate Word Cloud" button
def word_cloud_dialog():        
    top = tkinter.Toplevel()
    top.grab_set()
    option_frame = tkinter.Frame(top)
    option_frame.grid(row=0)
    top.title("Word Cloud Options")
    top.resizable(False, False)
    
    def on_dropdown_change(*args):
        text_op = default_text_op.get().lower().split(" ")
    
    # user has selected to generate word cloud
    def generate_wordcloud_btn_click():
        # create word cloud based on top tracks
        if default_text_op.get() == "Top Tracks":
            # creates list of top track long term in not in the cache
            tracks = spotify.get_top_tracks(limit=50, time_range="long_term") if not "tt-long_term" in cache else cache["tt-long_term"]
            cache["tt-long_term"] = tracks
            #creates list of song names
            track_list = []
            for t in tracks:
                track_list.append(t['name'])
            text = " ".join(track_list)
        # create word cloud based on top artists
        elif default_text_op.get() == "Top Artists":
            # creates list of top artists if not in the cache
            artists = spotify.get_top_artists(limit=50, time_range="long_term") if not "ta-long_term" in cache else cache[
                "ta-long_term"]
            cache["ta-long_term"] = artists
            #create list of artist names
            artists = cache["ta-long_term"]
            artists.reverse()
            artist_list = {}
            for a in range(len(artists)):
                artist_list[artists[a]['name']] = a
#           can switch with above for loop. Allows full artist name in word cloud
#            for a in artists:
#                artist_list.append(a['name'])
#            text = " ".join(artist_list)
            
#        Still can not get local font. Having trouble working with directories.     
#        font = default_font_op.get()
#        if font == "Select local font":
#            font = fd.askopenfilename()
#            font = os.path.dirname(os.path.abspath(font))
#        
        word_cloud_gen.generate(artist_list, prefer_horizontal=slider.get(), back_color=default_color_op.get(),font=default_font_op.get())
    
    #Content drop down menu
    text_options = ["Top Tracks", "Top Artists", "Lyrics"]
    default_text_op = tkinter.StringVar(option_frame)
    default_text_op.trace("w", on_dropdown_change)
    default_text_op.set(text_options[0])
    text_menu = tkinter.OptionMenu(option_frame, default_text_op, *text_options)
    text_menu.grid(row=0, column=2, padx=5, pady=5)
    
    #Color drop down menu
    color_options = ["black", "white", "blue", "magenta", "green", "random"]
    default_color_op = tkinter.StringVar(option_frame)
    default_color_op.trace("w", on_dropdown_change)
    default_color_op.set(color_options[0])
    color_menu = tkinter.OptionMenu(option_frame, default_color_op, *color_options)
    color_menu.grid(row=0, column=3, padx=5, pady=5)
    
    #Font drop down menu
    font_options = ["Marvind", "AlphaMusicMan", "Select local font"]
    default_font_op = tkinter.StringVar(option_frame)
    default_font_op.trace("w", on_dropdown_change)
    default_font_op.set(font_options[0])
    font_menu = tkinter.OptionMenu(option_frame, default_font_op, *font_options)
    font_menu.grid(row=0, column=4, padx=5, pady=5)
    
    slider = tkinter.Scale(option_frame, from_=0.0, to=1.0, resolution=0.1, label = "Horizontal Scale", length = 200, orient='horizontal')
    slider.set(0.6)
    slider.grid(row=0, column=1, padx=5, pady=5)
    generate_button = tkinter.Button(option_frame, text="Generate Word Cloud", width=20, height=2,
                                      command=lambda: generate_wordcloud_btn_click())
    generate_button.grid(row=0, column=0, padx=5, pady=5)
    


# Nathan TODO
def gen_rec_playlist_dialog():
    print()


# this shit broken
# I no good at maths, maybe someone cold figure it out lol
# I no use GUI, GUI is the devil
def center_in_screen(window):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width / 2) - 375  # can't figure out how to get current windows size
        y = (screen_height / 2) - 300
        window.geometry("+%d+%d" % (x, y))


if __name__ == "__main__":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # solves blurry tkinter widgets...thanks stack overflow
    main()
