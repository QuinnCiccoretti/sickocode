import pandas as pd
import pickle

df = pd.read_csv('lyrics.csv', sep=',')
df = df[df['genre'] == 'Hip-Hop']


def generate_data_struct():
    artists = df['artist'].unique().tolist()
    lyrics = dict()
    for each in artists:
        s = df[df['artist'] == each]['lyrics']
        lyrics[each] = s.str.cat(sep='\n\n')

    with open('lyrics.pk', 'wb') as handle:
        pickle.dump(lyrics, handle)

    with open('artists.pk', 'wb') as handle:
        pickle.dump(artists, handle)


def get_lyrics(artist):
    l_file = open('lyrics.pk', 'rb')
    lyrics = pickle.load(l_file)
    l_file.close()

    a_file = open('artists.pk', 'rb')
    artists = pickle.load(a_file)
    a_file.close()

    if artist in artists:
        return lyrics[artist]
    else:
        return lyrics[artists[1]]


generate_data_struct()

print(get_lyrics('drake'))
