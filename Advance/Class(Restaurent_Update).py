class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.number_served = 0
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine_type of the restaurant is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is now open...")

    def read_served(self):
        print(f"The number of customer has served is: {self.number_served}")

    def set_number_served(self, served):
        self.number_served = served
        # print("Upfate number served", served)

    def increment_served(self, new_served):
        self.number_served += new_served
        # print("Incremented Serve: ", new_served)


class user:
    def __init__(self, first_name, last_name, age, order_amount):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.order_amount = order_amount

    def describe_user(self):
        print(f"Name:   {self.first_name} {self.last_name}")
        print(f"Age:    {self.age}")
        print(f"amount: {self.order_amount}")

    def greet_user(self):
        print(f"Hello Mr. {self.first_name} {self.last_name}")
        print("Thank you for shopping with us..")


KFC = Restaurant("KFC", "FastFood")
JFC = Restaurant("JFC", "FastFood")
DFC = Restaurant("JFC", "CasualFood")

# JFC.describe_restaurant()
# print("")
# DFC.describe_restaurant()
# print("")

KFC.describe_restaurant()
print("")

first_customer = user("Atik", "Rahman", 25, 2000)
first_customer.describe_user()
first_customer.greet_user()
print()


KFC.number_served = 10
KFC.read_served()
KFC.set_number_served(20)
KFC.read_served()
KFC.increment_served(50)
KFC.read_served()


