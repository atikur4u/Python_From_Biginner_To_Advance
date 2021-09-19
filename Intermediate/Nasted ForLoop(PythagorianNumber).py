from math import sqrt

num = int(input("Enter the maximum number:"))
for a in range(1, num + 1):
    for b in range(a, num):
        c_sqrt = a ** 2 + b ** 2
        c = int(sqrt(c_sqrt))
        if c_sqrt - c ** 2 == 0:
            print(a, b, c)
