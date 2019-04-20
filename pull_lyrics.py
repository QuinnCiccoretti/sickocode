# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 02:31:31 2019

@author: homework
"""

#import lyricsgenius
#genius = lyricsgenius.Genius(client_access_token)
#artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
#song = genius.search_song("To You", artist.name)
#print(song.lyrics)
#print(artist.songs)
from tswift import Artist
import random
import time
def gen_lyrics(artist, filename):
    tswift = Artist(artist)
    
    songs = tswift.songs
    #print(songs.format())
    file = open(filename, 'w', encoding ='utf8')
    for i in songs:
        file.write("\nSON6\n")
        file.write(i.format())
        
    file.close()
start = time.time()
gen_lyrics('Travis Scott', 'test1')
end = time.time()
time = end - start
print(time)