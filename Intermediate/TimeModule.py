import time

"""Function of calculating the time of execution of loop."""
# initial = time.time()
#
# k = 0
# while k < 10:
#     print("this is atik vai")
#     k += 1
# print("while loop ran in ", time.time() - initial, "second")
#
# initial2 = time.time()
# for i in range(10):
#     print('This is atikur rahman')
# print("for loop ran in ", time.time() - initial2, "seconds")


"""Function of creating a clock"""
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
