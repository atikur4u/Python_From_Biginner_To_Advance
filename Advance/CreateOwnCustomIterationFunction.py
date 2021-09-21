class Iterator:
    def __init__(self, max):
        self.n = 0
        self.max = max

    def __Iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 1
            return result
        else:
            raise StopIteration
number = Iterator(10)
print(next(number))
print(next(number))