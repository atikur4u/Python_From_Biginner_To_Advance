row = int(input("Enter the number of row: "))
space = row-1
star = 1
for r in range(row):
    for s in range(space):
        print(" ", end="")
    space = space - 1
    for st in range(star):
        print(end="*")
    star = star+1
    print()