class Restaurant: 
    '''A class that stores information about a restaurant.'''
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


restaurant1 = Restaurant("O'Tacos", "French fast food")
restaurant2 = Restaurant("Pitaya", "Thai food")
restaurant3 = Restaurant("French Cantine", "French food")


restaurant1.describe_rest()
restaurant2.describe_rest()
restaurant3.describe_rest()

restaurant1.rest_open()
restaurant2.rest_open()
restaurant3.rest_open()