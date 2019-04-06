# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 02:31:31 2019

@author: homework
"""

#client id= "-rOq6wKsR7f9wM2gaIFsRwNxwD0_Q8DmVNWKGub3XeaOiPYF6wgYouRezaIhEYs9"
#client_secret= "122ZTjJTDcJ1YNG7T3Cm-AEcwOHoCNcTGXeDAXg2Ei7vIfox3Abl8s3CegWjxNW2FHY1bykZH3aGVJyPNVr4Mw"
#client_access_token= "sq1m7QDQ0sYqNyAeD_3d-ZVYRnpFuuTd4Nig9AyRYMnscs2oqSprj4TbHdFFcgMv"
#import lyricsgenius
#genius = lyricsgenius.Genius(client_access_token)
#artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
#song = genius.search_song("To You", artist.name)
#print(song.lyrics)
#print(artist.songs)
from tswift import Artist
import random
import time

tswift = Artist('Travis Scott')
start = time.time()
songs = tswift.songs
#print(songs.format())
file = open('testl.txt', 'w', encoding ='utf8')
for i in songs:
    file.write("\nSON6\n")
    file.write(i.format())
    
file.close()
end = time.time()
time = end - start
print(time)