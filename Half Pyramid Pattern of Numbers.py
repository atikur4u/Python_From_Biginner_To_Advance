row = int(input("Enter Your Number: "))
space = 1
star = 1

for r in range(row):
    for st in range(star):
        print("*", end="")
    print("")
    star = star + 1

star = star - 1
for r in range(row):
    for st in range(star):
        print("*", end="")
    print("")
    star = star - 1