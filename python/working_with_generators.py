

import numpy as np
from itertools import islice

x = np.arange(0,100)
def split_every(n, iterable):
    i = iter(iterable)
    piece = list(islice(i, n))
    while piece:
        yield piece
        piece = list(islice(i, n))

for chunk in split_every(5, x):
    print(chunk)
        
