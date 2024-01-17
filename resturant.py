class Restaurant():
    """ A simple resturant class """

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print(f"Restaurant name is: {self.resturant_name}")
        print(f"Cuisine is: {self.cuisine_type}")

    def open_restuarant(self):
        print(f"{self.resturant_name} is open")

class User:

    def __init__(self, first_name, second_name, location, payment_method):
        self.first_name = first_name
        self.second_name = second_name
        self.location = location
        self.payment_method = payment_method

    def describe_user(self):
        print(f"User first name: {self.first_name} \n" \
              f"User second name: {self.second_name} \n" \
              f"User location: {self.location} \n" \
              f"User payment method: {self.payment_method}")
    
    def greet_user(self):
        print(f"Welcome {self.first_name} {self.second_name}")

restaurants = [Restaurant('Dominos', 'Pizza'), Restaurant('Burger King', 'Burgers'), Restaurant('Wagamams', 'Asian')]
customers = [User('John', 'Smith', 'London', 'Cash'), User('Harry', 'Potter', 'Hogwarts', 'Card')]

for restaurant in restaurants:
    restaurant.describe_resturant()
    restaurant.open_restuarant()
    print("\n")

for customer in customers:
    customer.describe_user()
    customer.greet_user()
    print("\n")