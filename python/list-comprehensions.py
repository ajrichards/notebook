import types

## basic 
a = range(10)
b = [x**2 for x in a]
c = map(lambda x: x**2, a)
print(b)

print("-----")
## remove stuff
a = ['', 'fee', '', '', '', 'fi', '', '', '', '', 'foo', '', '', '', '', '', 'fum']
b = [x for x in a if len(x) > 0]
print(b)
print("-----")

## square only the ints
a = [1, '4', 9, 'a', 0, 4]
b = [ x**2 for x in a if type(x)==types.IntType ]
c = map(lambda x: x**2, filter(lambda x: type(x) == types.IntType, a))
print(b)
print(c)
print("-----")

## nested loops do not read like english
#flattened = [n for row in matrix for n in row]


## 
#doubled_odds = map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers))
#doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
