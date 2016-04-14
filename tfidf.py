import os, operator
from math import log

thisFile = open("./wsj/WSJ_2325", "r")
words = thisFile.readline().split(" ")

tf = {}
for word in words:
    tf[word] = tf.get(word, 0) + 1

idf = {}
collection = "./wsj/"
count = len(os.listdir(collection))
for word in words:
    wordFreq = 0

    for document in os.listdir(collection):
        fh = open(collection + document, "r")
        if word in fh.readline().split(" "):
            wordFreq += 1

    if wordFreq != 0:
        idf[word] = log(count / wordFreq)
    else:
        idf[word] = 0

tfidf = {}
for word in set(words):
    tfidf[word] = tf[word] * idf[word]

newA = sorted(tfidf.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]
print newA
newA = dict(sorted(tfidf.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])
print newA.keys()
