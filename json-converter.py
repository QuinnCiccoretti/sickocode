# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 01:18:06 2019

@author: Andrew Wang
"""

import json
import pull_lyrics
import true_ngrams
import os
artists = ['Travis Scott', 'Kanye West', 'Drake', 'Kendrick Lamar']
count = 0
everything = {}
for name in artists:
    raps = []
    count+=1
    pull_lyrics.gen_lyrics(name, 'testl.txt')
    true_ngrams.do('out_'+name+'.txt')
    file = open('out_'+name+'.txt', 'r')
    lyrics = file.read()
    raps.append(lyrics)
    everything[name] = raps
    
with open('raps.json', 'w') as outfile:
    json.dump(everything, outfile)
    
    #import true_ngrams
    #os.system('true_ngrams.py')