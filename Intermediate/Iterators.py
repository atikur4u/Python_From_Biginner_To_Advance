"""
-->>> Iterator: Iterator is an object that has __next__() method defined.
-->>> Iterable: Iterable is an object that gives you Iterators.
-->>> Iteration: The process where you iterate something of an object and fetch the next element of that object is
      called "Iteration".
"""
number = [1, 2, 3, 4]
print(dir(number))

values = number.__iter__()
print(values)  # This will give the address of the list where the list is stored
print(next(values))
print(next(values))

var = values.__next__()
print(var)
