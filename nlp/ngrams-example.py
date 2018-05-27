def get_ngrams(input, n):
  input = input.split(' ')
  output = {}
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output


all_words = 'hello wonderful world'
ngrams2 = get_ngrams(all_words, 2)
ngrams3 = get_ngrams(all_words, 3)
ngrams = dict(ngrams2, **ngrams3);

print(ngrams)
