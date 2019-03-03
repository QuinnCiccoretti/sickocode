import pandas as pd
import pickle

df = pd.read_csv('lyrics.csv', sep=',')
df = df[df['genre'] == 'Hip-Hop']
artists = df['artist'].unique()
lyrics = None


def generate_data_struct():
    global lyrics
    try:
        lyrics = open('lyrics.pk', 'rb')

    except FileNotFoundError:
        lyrics = dict()
        for each in artists:
            s = df[df['artist'] == each]['lyrics']
            lyrics[each] = s.str.cat(sep='\n@\n')

        with open('lyrics.pk', 'wb') as handle:
            pickle.dump(lyrics, handle)


def get_lyrics(artist):
    return lyrics[artist]


generate_data_struct()
print(get_lyrics('drake'))
