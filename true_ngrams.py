# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 04:19:45 2019

@author: Andrew Wang 
"""

# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import numpy as np
#import sklearn
from sklearn.model_selection import train_test_split
import nltk 

import pandas as pd
import time
#import pickle

df = pd.read_csv('lyrics.csv', sep=',')

def generate_data_struct(df):
    lyrics = df.sample(1000)#df[df['artist']==auteur]['lyrics'].to_frame().rename(columns = {0: 'lyrics'})
    #def rstrip(s):
    #    return s.replace('\r', '')
    lyrics_r = pd.Series()
    lyrics_n = list()
    for each in lyrics['lyrics']:
        #lyrics_n.append('SONG')
        s = str(each)
        s = s.replace('\r', '').split('\n')
        #print(s)
        s = [a + '\n' for a in s]
        copy = s
        for a in copy:
            if a[0] == '[':
                s.remove(a)
       
        lyrics_r = lyrics_r.append(pd.DataFrame(s))
        #lyrics_n = pd.DataFrame(lyrics_n)
    
    #lyrics['lyrics'] = lyrics['lyrics'].str.replace('\r', '').str.split('\n').str.concat('\n')
    #lyrics['lyrics'] = [s+'\n' for s in lyrics['lyrics'].str.split('\n') if s]
    #lyrics = pd.DataFrame(artists)
    print(lyrics_r.head(50))
    lyrics_r = lyrics_r.reset_index()
    return lyrics_r
gen = generate_data_struct(df)
gen = gen.sample(10000)
gen = gen[0]
gen = gen.replace(np.nan, '', regex=True)
gen = gen.rename(columns={0: 'text'})
gen = gen.reset_index()
gen = gen.drop(columns = ['index'])


    #print(lyrics['drake'])
#regex expressions
#chapters = r'^(?:SONG\s\d).*$'
chapters = r'SON6'
paragraphs = r'\n\n+'#r'^(\n\n+)*$'
sentences = r'([.;?!"“”]+)'
words = r'(\W+)'

#gen = df.sample(1000)


start = time.time()
time.clock()
text = open("testl.txt", 'r', encoding ='utf8').readlines() #read by line
end = time.time()
total = end-start
print(total)
text.append("\n")
#text = all_text[47: 8358] #keep only lines we want 
text = text[1:]

#df = generate_data_struct("eazy-e", df) 
df = pd.DataFrame(text, columns = ['text'])
frames = [df, gen]
result = pd.concat([df, gen], ignore_index = True, axis=0)
#def addp(s):
#    if(s=="\n"):
#        return s
#    elif("SON6" in s):
#        return s
#    else:
#        return s+". "
#df['text']=df['text'].apply(addp)
df.index.name = "line_num"
df = df.rename(columns={0: 'text'})

#def give_id(i):
#    return i.name 
#
#print(df.text.str.match(paragraphs).tolist())
#df.loc[df.text.str.match(paragraphs), 'prgrph_line_num'] = df.apply(give_id, 1)
#print(df.prgrph_line_num.tolist())
#df.prgrph_line_num = df.prgrph_line_num.fillna(method='bfill').astype('int')


#prgrph_index = df.prgrph_line_num.unique().tolist()
#def give_num(i):
#    return prgrph_index.index(i)+1
#df['pgr_num'] = df['prgrph_line_num'].apply(give_num)

#def join_lines(prgrph):
#    return ''.join(prgrph['text'])
#prgrph_text = df.groupby('pgr_num').apply(join_lines).to_frame()
#prgrph_text = prgrph_text.rename(columns={0:'pgr_strings'})

#prgrph = chapter_text['chapter_string'].str.split(paragraphs, expand = True).stack().to_frame() #expand separates splitted string into cols
#prgrph = prgrph.rename(columns={0:'pgr_strings'})
#prgrph.index.names = ['chapter_num', 'pgr_num']
start2 = time.time()
def give_id(i):
    return i.name 
df.loc[df.text.str.match(chapters), 'chapter_line_num'] = df.apply(give_id, 1)
df.chapter_line_num = df.chapter_line_num.ffill().astype('int')


chapter_index = df.chapter_line_num.unique().tolist()
def give_num(i):
    return chapter_index.index(i)+1
df['chapter_num'] = df['chapter_line_num'].apply(give_num)

def join_lines(chapter):
    return ''.join(chapter['text'])
chapter_text = df.groupby('chapter_num').apply(join_lines).to_frame()
chapter_text = chapter_text.rename(columns={0:'chapter_string'})

prgrph = chapter_text['chapter_string'].str.split(paragraphs, expand = True).stack().to_frame() #expand separates splitted string into cols
prgrph = prgrph.rename(columns={0:'pgr_strings'})
prgrph.index.names = ['chapter_num', 'pgr_num']

#cleaning based on the Moby Dick code 
prgrph.pgr_strings = prgrph.pgr_strings.str.strip() #separates everything
prgrph.pgr_strings = prgrph.pgr_strings.str.replace(r'\n', ' ') #replace newline with space
prgrph.pgr_strings = prgrph.pgr_strings.str.replace(r'\s+', ' ') #replace space(s) with space
prgrph = prgrph[~prgrph.pgr_strings.str.match(r'^\s*$')] #puts all unmatched strings into df

#endii = time2.time()
#timeii = endii-startii
#print(timeii)

#cleaning based on the Moby Dick code 
#prgrph_text.pgr_strings = prgrph_text.pgr_strings.str.strip() #separates everything
#prgrph_text.pgr_strings = prgrph_text.pgr_strings.str.replace(r'\n', ' ') #replace newline with space
#prgrph_text.pgr_strings = prgrph_text.pgr_strings.str.replace(r'\s+', ' ') #replace space(s) with space
#prgrph_text = prgrph_text[~prgrph_text.pgr_strings.str.match(r'^\s*$')] #puts all unmatched strings into df
#prgrph.pgr_strings.str.match(r'^\s*$')
#prgrph[~prgrph.pgr_strings.str.match(r'^\s*$')] #

#print(chapter_text.groups)


def st(line):
    return pd.Series(nltk.sent_tokenize(line))
sntnc = prgrph['pgr_strings'].apply(st).stack().to_frame()
        #.rename(columns={0:'pos_tuple'})
sntnc = sntnc.rename(columns={0:'sent_string'})
sntnc.index.names = ['chapter_num', 'pgr_num', 'sent_num']
del(prgrph)

#token = sntnc['sent_string'].str.split(words, expand = True).stack().to_frame() #expand separates splitted string into separate cols
def tokon(line):
    return pd.Series(nltk.pos_tag(nltk.word_tokenize(line)))
token = sntnc['sent_string'].apply(tokon).stack().to_frame()
token = token.rename(columns={0:'tokentuple'})
token.index.names = ['chapter_num', 'pgr_num', 'sent_num', 'token_num']
del(sntnc)

token['pos'] = token.tokentuple.apply(lambda x: x[1])
token['tokens'] = token.tokentuple.apply(lambda x: x[0])
token = token.drop('tokentuple', 1)

#print(token.head(100).to_string())

token['punc'] = token.tokens.str.match(r'^[\W_]*$').astype('bool')
token['number'] = token.tokens.str.match(r'\d').astype('bool')

end2 = time.time()
total2 = end2 - start2
print(total2)


start3 = time.time()
vocab = pd.DataFrame([token.tokens, token.punc, token.number]).transpose()
#vocab = vocab[(vocab['punc'] == False) & (vocab['number'] == False)]
vocab = vocab[(vocab['number'] == False)]
#vocab = vocab.drop(['punc', 'number'], axis = 1)

vocab['tokens'] = vocab['tokens'].str.lower().replace(r'[\'"_*.]', '')
vocab['tokens'] = vocab['tokens'].str.replace(r'_', '')
vocab = vocab['tokens'].str.lower().value_counts()
vocab =vocab.sort_index()
vocab = vocab.reset_index()
vocab = vocab.rename(columns = {'index': 'term', 'tokens':'frequency'})
vocab['id'] = vocab.index
vocab = vocab.set_index('term')


sw = pd.DataFrame(nltk.corpus.stopwords.words('english'), columns=['terms'])
def truth(s):
    return 1;
sw['s'] = sw['terms'].apply(truth)
sw = sw.set_index('terms')


#vocab['temp']=vocab['term']
#intersection = pd.merge(vocab, sw, on = 'terms')
vocab = vocab.join(sw)
vocab['s'] = vocab['s'].fillna(0)

vocab['term'] = vocab.index
vocab = vocab.set_index('id')

from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
vocab['temp'] = vocab['term']
vocab['p_stem'] = vocab['temp'].apply(stemmer.stem)

#def truth():
  # return 1
#intersection['s'] = intersection['terms'].apply(truth())
vocab = vocab.drop('temp', axis = 1)
#vocab = vocab.set_index('id')
end3 = time.time()
total3 = end3-start3
print(total3)
#nltk.help.upenn_tagset()
#print(token.index[:3])9'tg   
#pos=token.groupby(token.index.names[:3]).tokens.apply(lambda x: add_pos(x))
#pos=pos.rename(columns = {0: 'pos'})
start4 = time.time()
index_names = token.index.names
print(token.index.names[:2])
token['temp'] = token['tokens'].str.lower()
vocab['id']= vocab.index.astype(int)
temp = vocab[['term', 'id']]
temp = temp.set_index('term')
token = token.join(pd.DataFrame(temp['id']), on = 'temp')
token = token.drop('temp', axis = 1)
token['id'] = token['id'].fillna(-1)
token = token.rename(columns = {'id': 'token_id'})
vocab = vocab.rename(columns = {'id': 'term_id'})
print(token.index.names[:2])

ALL = token.groupby(token.index.names[:2]).apply(lambda x: np.random.choice(['train', 'test'], p=[.8, .2])).to_frame().rename(columns={0:'group'})
print(ALL.head())
token = pd.merge(token.reset_index(), ALL.reset_index(), on = token.index.names[:2])
token = token.set_index(index_names, drop=True)

train = token.groupby('group').get_group('train')
print(train.head())
print(len([token['group'] == 'test']))
test = token.groupby('group').get_group('test')

end4 = time.time()
total4 = end4 - start4
print(total4)
#print(test['tokens'].shape())

start5 = time.time()
def get_ngrams(tokens, n=2):
    
    # Create list to store copies of tokens table
    X = []
    
    # Add tokens without punc to list
    # Note: we assume that tokens has an OHC) multiindex
    X.append(token.tokens.reset_index())
    
    # Normalize the sequence number for token numbers for offsetting operation
    # Note: we assume that punc removal leaves a number series with regular gaps
    #X[0]['token_num'] = (X[0]['token_num'] / 2) 
    #X[0]['token_num'] = X[0]['token_num'].astype('int')
    
    # Create copies of token table for each level of ngram, offset by 1, and 
    # merge with previous
    IDX = ['chapter_num', 'pgr_num', 'sent_num', 'token_num'] 
    for i in range(1, n):
        X.append(X[0].copy())
        X[i]['token_num'] = X[i]['token_num'] + i
        #X[i] = X[i].merge(X[i-1], on=IDX, how='left', sort=True).fillna('<s>')
        X[i] = X[i].merge(X[i-1], on=IDX, how='left', sort=True).fillna('<s>')
        #X = X[pd.notnull(X[i])]
    # Compress tables to unique ngrams with counts
    for i in range(0, n):
        X[i] = X[i].drop(IDX, 1)
        cols = X[i].columns.tolist()
        X[i]['n'] = 0
        X[i] = X[i].groupby(cols).n.apply(lambda x: x.count()).to_frame()
        X[i].index.names = ['w{}'.format(j) for j in range(i+1)]
    
    # Return just the ngram tables
    return X


print(train.head())
UGM, BGM, TGM = get_ngrams(train, n=3)
UGT, BGT, TGT = get_ngrams(test, n=3)

end5 = time.time()
total5 = end5-start5
print(total5)
#print(TGM.head(20))
def align_model(ngm, ngt):
  idx = ngm.index.names
  ngm = pd.merge(ngm.reset_index(), ngt.reset_index(), on=idx, how='outer').fillna(1).set_index(idx)
  ngm = ngm.rename(columns={'n_x':'n'})
  ngm = ngm.drop('n_y', 1)
  return ngm

UGM = align_model(UGM, UGT)
BGM = align_model(BGM, BGT)
TGM = align_model(TGM, TGT)

#print(TGM.head(25))
def infer_probs(ngm):
    if len(ngm.index.names) > 1:
        ngm['p'] = ngm.groupby(ngm.index.names[:-1]).n\
            .apply(lambda x: x / x.sum())\
            .to_frame().rename(columns={'n':'p'})
    else:
        ngm['p'] = ngm['n'] / ngm['n'].sum()
    ngm['logp'] = np.log2(ngm['p'])
    ngm['h'] = ngm.logp * ngm.p * -1
    return ngm

UGM = infer_probs(UGM)
BGM = infer_probs(BGM)
TGM = infer_probs(TGM)

def perplexity(ngm, ngt):
    pp = np.exp2(-(ngm['logp'] * ngt['n']).sum() / ngt['n'].sum())
    return round(pp, 2)

ppu = perplexity(UGM, UGT)
ppb = perplexity(BGM, BGT)
ppt = perplexity(TGM, TGT)
print("perplexity:", ppt)
test = ''
n = 1000
#print(TGM.head(100))
TGM = TGM.sort_index()
#BGM = BGM.sort_index()
idx = TGM.index.names
#idx = BGM.index.names
#print(idx)
tg = TGM.sample().reset_index()[idx].values.tolist()[0]
#tg = BGM.sample().reset_index()[idx].values.tolist()[0]
test += ' '.join(tg) #+ ' ...'
for i in range(n):
    key = tuple(tg[1:])
    weights = TGM.loc[key, 'p']
    w2 = TGM.loc[key].sample(weights=weights)\
        .reset_index()[idx[-1]].values.tolist()[0]
    
    if w2 == '<s>':
        continue
    
    tg = tg[1:] + [w2]
    if i % 10 == 1:
        test += '\n'
    else:
        test += ' '
    test += w2
    
import language_check
tool = language_check.LanguageTool('en-US')
matches = tool.check(test)
print(len(matches))
#if(len(test)>100):
#    print(test[:100])
#else:
print('RAW-OUTPUT:')
print(test)
print()
print('SPELL-CHECK OUTPUT:')
print(language_check.correct(test, matches))


