# 4. How do you calculate the distance between coordinates (x1, y1) and (x2, y2)? Hint:
# You'll need to look up how to calculate a square root in Python, which may involve a
# function from the math module

import math

x1 = 5.2
y1 = 2

x2 = 9
y2 = 3.9

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between the two points is: {distance:.2f}")