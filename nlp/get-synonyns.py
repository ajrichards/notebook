#!/usr/bin/env python
"""
>>> import nltk
>>> nltk.download('wordnet')

hypernyms - are the 'is a' relationships

"""

from nltk.corpus import wordnet as wn


panda = wn.synset('panda.n.01')
hyper = lambda s: s.hypernyms()
syns = list(panda.closure(hyper))

print(syns)
