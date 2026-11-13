# 2. How do you calculate the area of a rectangle?

Length = int(input('Enter the lenght: '))
Width = int(input('Enter the width: '))

Area = Length * Width

print('Side A is', Length)
print('Side B is', Width)
print('The area of the rectangle is', Area)

# When I first typed length/width = input('Enter the length/width: '), I got an error message
# displayed in the terminal saying that I couldn't multiply strings. So I had to
# convert the input values to integers.