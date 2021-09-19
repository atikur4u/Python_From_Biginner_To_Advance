import random


randnumber = random.randint(1, 20)
guess = 0
while guess != randnumber:
    randnumber = random.randint(1, 20)
    guess = int(input("Enter number: "))
    if guess > 0:
        if guess > randnumber:
            print("The number is large then Guessed number..")
            print("The Random number is ",randnumber)
        elif guess < randnumber:
            print("The number is small then Guessed number.. ")
            print("The Random number is ",randnumber)
    else:
        print("Sorry. You are giving up..")
        break
else:
    print("Congratulation. You have made it..")
    print("The Random number is ", randnumber)
