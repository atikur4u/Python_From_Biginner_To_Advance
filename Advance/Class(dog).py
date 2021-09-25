class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


tommy = Dog("Tommy", 13)
print(f"My dog's name is {tommy.name}. His age is {tommy.age}")
tommy.sit()
tommy.roll_over()

print("")

lucy = Dog("Lucy", 6)
print(f"My dog name is {lucy.name}. Her age is {lucy.age}")
lucy.sit()
lucy.roll_over()

