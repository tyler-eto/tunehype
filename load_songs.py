import os
import sys
import django

import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tunehype.settings")

django.setup()

from reviews.models import Song


def save_song_from_row(song_row):
    wine = Song()
    wine.id = song_row[0]
    wine.name = song_row[1]
    wine.save()


if __name__ == "__main__":

    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        wines_df = pd.read_csv(sys.argv[1])
        print(wines_df)

        wines_df.apply(save_song_from_row, axis=1)

        print("There are {} wines".format(Song.objects.count()))

    else:
        print("Please, provide Wine file path")
