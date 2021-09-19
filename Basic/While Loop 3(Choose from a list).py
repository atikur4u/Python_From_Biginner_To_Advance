import random

foo = ['a', 'b', 'c']
randnum = random.SystemRandom()
guess = 'd'
print(randnum.choice(foo))
while guess != randnum:
    randnum = random.SystemRandom()
    guess = input("Enter number: ")
    if guess != 'd':
        if guess > randnum:
            print("The number is large then Guessed number..")
            print("The Random number is ", randnum.choise(foo))
        elif guess < randnum:
            print("The number is small then Guessed number.. ")
            print("The Random number is ", randnum.choise(foo))
    else:
        print("Sorry. You are giving up..")
        break
else:
    print("Congratulation. You have made it..")
    print("The Random number is ", randnum.choise(foo))
