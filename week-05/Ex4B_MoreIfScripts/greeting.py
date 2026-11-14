current_hour = int(input('Enter time: '))

if 0 <= current_hour < 10:
    print('Good morning!')
elif 10 <= current_hour < 17:
    print('Good day!')
elif 17 <= current_hour <= 23:
    print('Good evening!')
else:
    print('Invalid time')


# or 

current_hour = int(input('Enter time: '))

if 0 <= current_hour < 10:
    print('Good morning!')
elif current_hour < 17:
    print('Good day!')
elif current_hour <= 23:
    print('Good evening!')
else:
    print('Invalid time')

if current_hour == 23 or 0 <= current_hour <= 4:
    print('What are you doing up so late?')


# There is no need to include 10 <=  or  17 <=  in the conditions.
# Python checks the conditions in order. If current_hour < 10 is False, it moves to the next condition.
# Since 10 is not less than 10, Python moves to the next condition.
#
# The same logic applies to current_hour < 17. If it is False, Python moves to the next condition.
# Since 17 is not less than 17, Python moves to the next condition.

