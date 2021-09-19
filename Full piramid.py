row = int(input("Enter the number of row:"))
star = 1
space = row - 1
for r in range(row):
    for sp in range(space):
        print(" ", end="")

    for st in range(star):
        print("*", end="")
    print()

    space -= 1
    star = star + 2

row = row - 1
space = space + 2
star = star - 4
for r in range(row):
    for sp in range(space):
        print(" ", end="")

    for st in range(star):
        print("*", end="")
    print()

    space += 1
    star = star - 2

print("************ If you want to simplify the code then uncomment the below code ************")

'''
row = 5
for i in range(row):
    print(" "*(row-i-1)+"* "*(i+1))
    #i+=1

for j in range(row):
    print(" "*(j+1)+"* "*(row-j-1))
    #j-=1
'''
