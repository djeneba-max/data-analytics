favorite_movies = [
    "The Lion King",
    "Charlie and the Chocolate Factory",
    "Sanoudje"
]

print(len(favorite_movies))

print('The list favorie_movies includes my top ' + str(len(favorite_movies)) + ' favorite movies.')
print(favorite_movies)
# a)
print(sorted(favorite_movies))
print(favorite_movies)
# The first output displays the list in alphabetical order, 
# while the second displays the movies in the original order they were entered.

# b)
favorite_movies.sort()
print(favorite_movies)
# Both methods produce the same output (the list in alphabetical order), 
# but the first uses `print(sorted(favorite_movies))`, while the second sorts the original list first using `.sort()` and then prints it.

favorite_movies.append("Desert")
print(favorite_movies)

print('The list favorie_movies includes my top ' + str(len(favorite_movies)) + ' favorite movies.')