"""
-->>> Generator is a route line that can be used to control the Iteration behavior of a loop.
-->>> All the generator are also iterator.
-->>> Generator means not to print something but to capable to generate given number of element.
-->>> Generator will not use your ram but will capable to work with those elements.

-->>> "yield" is a keyword that will not use your ram but will generate given number of element.
"""


def gen(n):
    for i in range(n):
        yield i


print(gen(10000000))
for b in gen(10000):
    print(b)
