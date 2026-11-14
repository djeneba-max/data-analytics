fruit_candies = ("Gummies", "Lollipops", "Jelly beans")
fruity_flavors = ("Strawberry", "Mango", "Watermelon")


candy_combinations = {
    fruit_candies[0] + " " + fruity_flavors[1],
    fruit_candies[1] + " " + fruity_flavors[0],
    fruit_candies[2] + " " + fruity_flavors[2]
} 

print("Today’s candy options include: ")
print(candy_combinations)

# The order of the items changes when I repeat the output because sets are unordered collections.