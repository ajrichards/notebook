import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np

## count vectorizer expects a list of strings
text1 = "oh the thinks you can thing if only you try"
text2 = "you can think up a guff going by if you try"
text3 = "i am a guff you are a guff we are all guffs"

corpus = [text1,text2,text3]
 
## count vectorizer for 1-grame
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(corpus)
features = vectorizer.get_feature_names()
matrix = counts.toarray()
print(features)
print(matrix)

## count vectorizer for bi-grams
bigram_vectorizer = CountVectorizer(ngram_range=(1, 2),token_pattern=r'\b\w+\b', min_df=1)
counts = bigram_vectorizer.fit_transform(corpus)
features = bigram_vectorizer.get_feature_names()
matrix = counts.toarray() 
print(features)
print(matrix)

## use tfidf to transform the occurances into relative frequencies
transformer = TfidfTransformer(smooth_idf=False)
tfidf = transformer.fit_transform(counts)
tfidf_matrix = tfidf.toarray()
print(np.round(tfidf_matrix,2))

## the same result can be obtained with the tfidf class
## Occurrence count is a good start but there is an issue: l
## longer documents will have higher average count values than shorter documents, even though they might talk about the same topics.

