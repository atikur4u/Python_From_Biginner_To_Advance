num = int(input("Enter the Maximum number: "))

for a in range(1, num):
    for b in range(num, 0, -1):
        print(b, end=", ")
    print("")

num = int(input("Enter the Maximum number: "))

for a in range(1, num + 1):
    for b in range(a, num + 1, 1):
        print("*", end=" ")
    print("")
