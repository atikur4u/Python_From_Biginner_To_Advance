x = int(input("Enter a Number: "))
if x > 5:
    raise Exception('Input value should not exceed 5. The input is {}'.format(x))
else:
    print("Congratulation You have enter the correct number.")
