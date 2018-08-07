#!/usr/bin/env python

'''
python -m spacy download en_core_web_md

spacy has a number of models and languages

https://spacy.io/usage/models


'''


import spacy
spacy.load('en_core_web_md')

nlp = spacy.load('en_core_web_md')

# process a sentence using the model
doc = nlp("This is some text that I am processing with Spacy")

# It's that simple - all of the vectors and words are assigned after this point

# Get the vector for 'text':
doc[3].vector

# Get the mean vector for the entire sentence (useful for sentence classification etc.)
doc.vector


