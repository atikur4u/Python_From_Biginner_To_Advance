num = [1, 3, 4]
iter_obj = iter(num)
# print(iter_obj.__next__())

while True:  # Here this is a loop without any condition. This loop will run until the break condition execute.
    try:
        element = next(iter_obj)
        print(element)

    except StopIteration:
        break
