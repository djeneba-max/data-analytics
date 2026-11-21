# ============================================================
# FUNCTIONS: print(), return, PARAMETERS, ARGUMENTS AND SCOPE
# ============================================================


# Defining a function

def function_example(ex):           # When I call the function,
    print('Argument example:', ex)  # Python executes this part (anything under the function).


# EXAMPLE 1:    

def favorite_food(food):
    print('I love', food)

# Here, calling the function will execute the print statement.
# Our objective is simply to display something.


#=========================================================================================================
# We use print() inside a function when we only need to display something to the screen.
# We use return inside a function, when we want the function to produce a result that we can reuse.
# You can store this result/value in a variable.
# You can also directly use it in a print() statement.
#=========================================================================================================


# EXAMPLE 2: return inside a function

def favorite_drink(drink):
    return drink

# return sends a value back from the function. 
# Here, the function returns the value passed to the parameter 'drink'.
# If I returned something else, that would be the value returned.




# EXAMPLE 3: Storing the returned value in a variable

result = favorite_drink('fanta')

print(result)

# Here, Python stores the returned value ('fanta') in the variable 'result'.
# I can now reuse this value elsewhere in my program.




# EXAMPLE 4: Displaying the returned value directly with print() statement

print(favorite_drink('fanta'))

# Python executes the function first.
# The function returns 'fanta'.
# Then print() displays the returned value.


#=========================================================================================================
# REMEMBER: 
# A parameter is a local variable defined in a function. It can only be accessed inside that function.

# Parameter = the variable defined in the function.
# Argument = the actual value passed to the function/parameter.

# If I try to access a local variable outside the function, I will get a NameError.
#=========================================================================================================


# EXAMPLE 5: Understanding VARIABLE SCOPE

def favorite_food(food):           # defining the function
    print('I love', food)

favorite_food('apple')             # calling the function 

#print(food)                       # trying to use the local variable outside the function


# The argument 'apple' is passed to the parameter 'food'.
# 'food' is a LOCAL VARIABLE because it is defined inside the function.

# Once Python finishes executing the function, I cannot access 'food' from outside the function.
# print(food)  # NameError: name 'food' is not defined


#=========================================================================================================
# Assigning a value to a parameter when calling a function does not automatically 
# create a variable accessible outside that function.



# Python executes the function, returns a value if there is
# a return statement, then continues with the rest of the program.
#=========================================================================================================