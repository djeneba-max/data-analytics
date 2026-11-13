import math
tourists = 38
van_places = 15
van_rent = 250

van_needed = math.ceil(tourists/van_places)
rental_price = van_rent*van_needed
print(f'van needed: {van_needed}')
print(f'Rental price: ${rental_price}')

price_per_tourists = rental_price/tourists
print(f'Each person will pay ${price_per_tourists:.2f}.')

# a) $19.74
# b) 19.74*38 = 750.12
# c) The rental price for the vans was $750
# d) Because we had to round up the amount charged per person, 
# # so we collected more money than necessary to cover the cost of the vans.