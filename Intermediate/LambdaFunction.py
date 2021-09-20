# First function without Lambda Function
def add(a, b):
    return a + b


# Second function with Lambda function
minus = lambda a, b: a - b
print(add(2, 8))
print(minus(8, 3))

# Third Function with list sorting with Lambda Function
a = [[1, 2], [5, 23], [8, 14]]
a.sort(key=lambda x: x[1])
print(a)

larger = lambda a, b: a if a > b else b
print(larger(1, 8))
