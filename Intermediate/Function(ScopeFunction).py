x = 89
def harry():
    x = 20

    def rohan():
        global x
        x = 40

    print("before calling rohan ", x)
    rohan()
    print("after calling rohan ", x)

harry()
print(x)
'''Here first the program set the value of x = 89.
then it will call the harry function then it will change the value of x into 40
so it will print the x value 40...'''