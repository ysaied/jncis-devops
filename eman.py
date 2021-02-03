#!/usr/bin/python3
import pandas as pd # Importing the libraries
import numpy as np
import os
#import nltk
#import heapq 
from nltk.tokenize import sent_tokenize, word_tokenize
#from nltk.tokenize import word_tokenize
import re
import csv
#not found
#from PIL import Image
from os import path
#from PIL import Image
from scipy.sparse import coo_matrix
from sklearn.feature_extraction.text import TfidfTransformer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer
#CountVectorizer(dtype=int32)
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer 
from nltk.corpus import stopwords

#nltk.download('stopwords')
corpus = []
stopwords = nltk.corpus.stopwords.words('english')


dataset = pd.read_csv('/var/tmp/eman.csv',delimiter="\t",encoding='UTF-8')# Importing the dataset
dataset.head()

num_words = 0


with open('/var/tmp/eman.csv',encoding='UTF-8',errors='ignore') as f:
   for text in f:
        #print(f.read())
        words = text.split()
        num_words += len(words)
        sentence =text.count('.') + text.count('!') + text.count(';') + text.count(':') + text.count('?')
        words = len(text.split())
        syllable = 0
        sentence_list = nltk.sent_tokenize(text)  
        for word in text.split():
            for vowel in ['a','e','i','o','u']:
                syllable = syllable + word.count(vowel)
            for ending in ['es','ed','e']:
                if word.endswith(ending):
                    syllable  = syllable - 1
                if word.endswith('le'):
                    syllable  = syllable + 1
sentence_scores = {}  
stopwords = nltk.corpus.stopwords.words('english')
print('word_frequencies')
word_frequencies = {} 


with open('/var/tmp/eman.csv',encoding='utf-8',errors='ignore') as f:
    for text in f:
        for word in nltk.word_tokenize(text):  
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1


for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
    print('sentence_list')
    print(sentence_list)
import heapq  
summary_sentences = heapq.nlargest( 3, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)  
print('summary')  
print(summary)  
# Removing Non-ASCII characters
def remove_non_ascii_1(dataset):
       return ''.join([i if ord(i) < 128 else ' ' for i in dataset])
#print(dataset)
corpus = []
stopwords = nltk.corpus.stopwords.words('english')
with open('/var/tmp/eman.csv',encoding='utf-8',errors='ignore') as f:
    for text in f:
       # normalize certain words
        text = re.sub("\\s+[a-zA-Z0-9]\\s+"," _connector_ ",text)
        #Remove punctuations
        text = re.sub('[^a-zA-Z]', ' ', text)# Search for all non-letters
    #Convert to lowercase
        text = text.lower()
    #remove tags
        text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    # remove special characters and digits
        text=re.sub("(\\d|\\W)+"," ",text)
    ##Convert to list from string
        text = text.split()
        ##Stemming
        ps=PorterStemmer()
    #Lemmatisation
        lem = WordNetLemmatizer()
        text = [lem.lemmatize(word) for word in text if not word in  stopwords] 
        text = " ".join(text)
        corpus.append(text)
        #print(corpus[:])
wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=200,
                          max_font_size=50, 
                          random_state=42
                         ).generate(str(corpus))
print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("word1.png", dpi=900)
# Creating the Bag of Words model5
cv=CountVectorizer(max_df=10,stop_words=stopwords, max_features=10000, ngram_range=(1,3))
X=cv.fit_transform(corpus)
list(cv.vocabulary_.keys())[:30]
print('list of key')
print(list(cv.vocabulary_.keys())[:30])
#cv.stop_words
#print(cv.stop_words)
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(X)
print("x")
print(X)
class CustomVectorizer(CountVectorizer): 
    def build_analyzer(self):
        """Return a callable that handles preprocessing and tokenization"""
        if callable(self.analyzer):
            return self.analyzer
        preprocess = self.build_preprocessor()
        if self.analyzer == 'char':
            return lambda doc: self._char_ngrams(preprocess(self.decode(doc)))
        elif self.analyzer == 'char_wb':
            return lambda doc: self._char_wb_ngrams(
                preprocess(self.decode(doc)))
        elif self.analyzer == 'word':
            tokenize = self.build_tokenizer()
            lemmatize = lambda doc: \
                    [ps.stem(token) for token in doc]

            stop_words = self.get_stop_words()

            return lambda doc: self._word_ngrams(
                lemmatize(tokenize(preprocess(self.decode(doc)))),
                stop_words)
        else:
            raise ValueError('%s is not a valid tokenization scheme/analyzer' % self.analyzer)
sentences = ['The quick brown fox.','Jumps over the lazy dog!']
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
vec = CustomVectorizer(lowercase=True,analyzer='word', ngram_range=(2, 2),tokenizer = token.tokenize)
text_counts = vec.fit_transform(sentences)    

print('text_counts')
print(text_counts)
list(cv.vocabulary_.keys())[:10]
feature_names=cv.get_feature_names()
print('feature_names')
print(feature_names)
