print("Welcome to Brac bank ATM System")

balance = 100
chances = 3
restart = 'Y', 'y'

while chances > 0:
    pin = int(input("Enter your pin: "))
    if pin == 1234:
        print("Pin accepted....")

        while restart not in ('n', 'N', 'No', 'no'):
            print('''Please chose one option:
            1. Check Balance
            2. Balance withdrew
            3. Pay In
            4. Return card''')
            option = int(input())
            if option == 1:
                print("your balance is ", balance, "$")
                restart = input("Would you like to go back?")
                if restart in ('n', 'N', 'no', "No"):
                    print('Thank You...')
                    break
                else:
                    continue
            elif option == 2:
                withdraw = int(input("Enter the amount: "))
                print(withdraw, "$ has been withdrawal.\n Now your balance is ", balance - withdraw, "$")
                restart = input("Would you like to go back?")
                if restart in ('n', 'N', 'no', "No"):
                    print('Thank You...')
                else:
                    continue

            elif option == 3:
                pay_in = int(input("Enter the amount you want to deposit: "))
                print(pay_in, " $ has been deposited in your account. Your balance is ", balance + pay_in)
                restart = input("Do you want to go back?")
                if restart in ('n', 'no', 'N', 'No'):
                    print("Thank You...")

            elif option == 4:
                rc = input("Do you want to return your card?")
                if rc in ('y', 'Y', 'yes', 'Yes'):
                    print("Thank you for take our service.")
                    break

    elif pin != 1234:
        chances -= 1
        print("Wrong password...")
        if chances <= 0:
            print("Sorry.. No more tries...")
            break
