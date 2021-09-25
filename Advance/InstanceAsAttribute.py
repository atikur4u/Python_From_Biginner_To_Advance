class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print(f"{self.year} {self.make} {self.model}")

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class electric_car(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batterysize = 75
        self.battery = Battery()  # Here we initialize the battery class an attribute...


"""Here we are braking a big class into a smaller class."""


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describeBattery(self):
        print(f"This car has a {self.battery_size} kwh battery.")


mytesla = electric_car('Tesla', 'Model S', 2019)
mytesla.get_descriptive_name()
mytesla.battery.describeBattery()
