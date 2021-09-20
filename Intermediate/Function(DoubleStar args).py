#We use "**args for unknown number of KEYWORD ARGUMENT to pass through a function
# This will work as dictionary
def user(**user):
    print(user)


user(id=1, name="atik", age=23)
