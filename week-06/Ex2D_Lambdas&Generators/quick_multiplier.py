doubler = lambda n: n * 2

# lambda indicates that we are creating a function without using def.
# doubler is the variable name used to store the function.
# The colon separates the parameter from the expression to be executed.

# TEST
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))
print()





tripler = lambda n: n * 3

# TEST 
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))
print()




# MORE MULTIPLIERS
def multiplier(x):
    return lambda n: n * x
# This function allows us to create multiple multiplier functions by providing different factors,
# instead of writing a separate function for each multiplier.

times4 = multiplier(4)
times5 = multiplier(5)
times6 = multiplier(6)
times7 = multiplier(7)
times8 = multiplier(8)
times9 = multiplier(9)
times10 = multiplier(10)


# TEST 
print(times4(2))
print(times5(2))
print(times6(2))
print(times7(2))
print(times8(2))
print(times9(2))
print(times10(10))

