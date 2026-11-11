print('Hello world!')

message = 'Hello world!'
print(message)

# "Hello world" prints twice because there are two print() statements in the code.
# The first print() displays 'Hello world!' directly.
# The second print() displays the value assigned to the variable 'message'.


# Displaying dollars and cents
dollars = 3
cents = .50
print(dollars + cents)
# I've noticed that the two variables were added together, which resulted in 3.5.


cents = cents + .25
print(dollars + cents)
# The new result is 3.75, after updating the value of 'cents'.

d_str = '3 dollars'
c_str = ' 50 cents'
print(d_str + c_str)
# or print(d_str + ' ' + c_str), with c_str = '50 cents'.