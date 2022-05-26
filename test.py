# it is my scribbles

import itertools


a = [[1,2],[3,4],[5,6]]
a = list(itertools.chain.from_iterable(a))
print(a)