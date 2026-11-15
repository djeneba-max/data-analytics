a= 1
b = 6
c = 5

if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c


print(f'The smallest number is {smallest}')
print(f'The largest number is {largest}')


# If we were to use min() and max()
# smallest = min(a, b, c)
# largest = max(a, b, c)

# print(f'The smallest number is {smallest}')
# print(f'The largest number is {largest}')