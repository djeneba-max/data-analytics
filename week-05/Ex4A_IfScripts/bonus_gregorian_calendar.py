year = 2000

if year % 400 == 0:
    print(year, 'is a leap year.')
elif year % 100 == 0:
    print(year, 'is not a leap year.')
elif year % 4 == 0:
    print(year, 'is a leap year.')

else:
    print(year, 'is not a leap year.')


# To determine whether a year is a leap year, we first check if it is divisible by 400 (leap year).
# If not, we check if it is divisible by 100 (not a leap year).
# Finally, we check if it is divisible by 4 (leap year).
# If none of these conditions are met, it is not a leap year.