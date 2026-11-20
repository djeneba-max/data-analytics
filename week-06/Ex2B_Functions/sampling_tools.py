import random 

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector'] 
print(products) # Added to better understand how shuffle() works.

# a)
print("Product of the Day:", random.choice(products)) 
# Selects one random item from the list.



# b)
survey_products = random.sample(products, 3)
print("Products selected for the survey:", survey_products)
# Selects 3 random items from the list without selecting the same item more than once.



# c)
random.shuffle(products)
print("Products in randomized order:", products)

# shuffle() does not return a value (it returns None); instead, it directly modifies the original list.
# print() displays the list after shuffling.
# Separate the shuffle() and print() instructions: 
# random.shuffle(products)
# print("Products in randomized order:", products)

# d) 
daily_transactions = random.randint(50, 300)
print("Daily transaction count:", daily_transactions)