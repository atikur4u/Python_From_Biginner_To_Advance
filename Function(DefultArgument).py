def increment(num, by=1):
    # To set the value of parameter in the function call default argument
    # All the default parameter should comes after the unassigned parameter.
    # If default parameter comes before the unassigned parameter then the function will give an error
    return num + by


print("The increment is ", increment(5, 5))
# Now if we pass two argument then it will consider the 2nd value as the value of second variable
# Otherwise the default value will be the 1 of 2nd variable
