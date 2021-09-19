# Here we use (*argument) for unknown number of arguments ....

def multiply(*number):
    total = 1
    for num in number:
        total *= num
    return total


print(multiply(2, 3, 3))
