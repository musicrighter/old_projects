list(map(str.capitalize, ['alpha', 'beta', 'gamma', 'delta', 'epsilon']))
['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']


s = '     Marcus was in BC 127 -- 186'

list(filter(str.isalpha, s.split()))
['Marcus', 'was', 'in', 'BC']


x = '  -- Marcus Tullius Cicero (106 BC -- 43 BC)'

list(map(lambda x: x.strip(punctuation), s.split()))
['Marcus', 'Tullius', 'Cicero', '106', 'BC', '43', 'BC']


>>> from operator import mul
>>> mul(6, 7)
42

>>> reduce(mul, range(1, 8))
5040


>>> from operator import add
>>> reduce(add, range(10))
45

sum(range(10))
45


>>> f = lambda x: x.strip(punctuation)
>>> f

>>> f('...hi...')
'hi'