# song-alyze
# Authors: Nathan Breunig, Kylei Hoffland, Giannia Lammer, Jon Noel
# LAST MODIFIED: 3/26/20
from . import spotify


def main():
    print(spotify.get_top_tracks(limit=10, time_range="short_term"))


if __name__ == "__main__":
    main()
