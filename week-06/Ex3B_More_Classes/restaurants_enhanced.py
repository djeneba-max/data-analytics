
class Restaurant: 
    '''A class that stores information about a restaurant.'''
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0           # default attribute, initialise the number served to 0
        self.customer_ratings = []       # default attribute, empty list

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        customers = int(input("How many customers served today? "))
        self.number_served += customers  # Adds the number of customers to the existing number_served value.

    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers.')

    def customer_rating(self):
        while True:
            try:
                rating = int(input('How would you rate your experience today on a scale of 1-5 (5 being excellent)?'))
                if rating < 1 or rating > 5:
                    print("Invalid rating. Please enter a number between 1 and 5.")
                else:
                    break

            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 5.")
            

        self.customer_ratings.append(rating)  # .append() because self.customer_ratings is a list.

        average_rating = sum(self.customer_ratings) / len(self.customer_ratings)
            # or average_rating = statistics.mean(self.customer_ratings), with import statistics
        
        print(f'Your rating was {rating}.\nThe average rating for this restaurant ({self.rest_name}) is{average_rating: .1f}.')



# With while True, Python exits the loop when it encounters a True condition with a break.

restaurant1 = Restaurant("O'Tacos", "French fast food")
restaurant2 = Restaurant("Pitaya", "Thai food")
restaurant3 = Restaurant("French Cantine", "French food")


restaurant1.describe_rest()
restaurant2.describe_rest()
restaurant3.describe_rest()
print()
restaurant1.rest_open()
restaurant2.rest_open()
restaurant3.rest_open()
print()
# a)
# restaurant1

restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()
print()

# restaurant2

restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()
print()

# restaurant3

restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()
print()


# b)
# restaurant1
restaurant1.customer_rating()
restaurant1.customer_rating()
restaurant1.customer_rating()
print()

# restaurant2
restaurant2.customer_rating()
restaurant2.customer_rating()
restaurant2.customer_rating()
print()


# restaurant3
restaurant3.customer_rating()
restaurant3.customer_rating()
restaurant3.customer_rating()
print()

# c)
