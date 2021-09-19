print("Calculate Factorial...")
n = int(input("Enter a number: "))
factorial = 1
if n > 0:
    for i in range(1, n + 1):
        factorial = factorial * i
    print("The Factorial of ", n, " is", factorial)
elif n == 0:
    print("The Factorial of 0 is 1")
else:
    print("The value should be a positive number...")
