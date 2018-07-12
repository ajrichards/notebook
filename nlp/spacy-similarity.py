#!/usr/bin/env python
'''
https://spacy.io/usage/vectors-similarity

python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md

'''


import spacy

nlp = spacy.load('en_core_web_md')  # make sure to use larger model!
tokens = nlp(u'dog cat banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
