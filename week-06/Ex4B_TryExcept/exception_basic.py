# ValueError

try:
    age = int("hello")

except ValueError:
    print("ValueError: You cannot convert this string into an integer.")

else:
    print(age)

finally:
    print("Let's try another one...")

# A ValueError occurs when a function receives a value of the correct type, but the value is not acceptable.






# NameError

try:
    print(student_name)

except NameError:
    print("NameError: This variable has not been defined.")

else:
    print(student_name)

finally:
    print("Let's try another one...")

# A NameError occurs when Python encounters a name (variable, function, etc.) that has not been defined.






# TypeError

try:
    result = "Hello" + 5

except TypeError:
    print("TypeError: You cannot concatenate a string and an integer.")

else:
    print(result)

finally:
    print("Let's try another one...")

# A TypeError occurs when you try to perform an operation with incompatible data types.




# SyntaxeError

try:
   eval("print('Hello'")    

except SyntaxError:
    print("SyntaxError: You have a syntax error in your code.")

else:
    print("No error!")

finally:
    print("Let's try another one...")

# A SyntaxError occurs when the code does not follow Python's syntax rules.
# eval() is a function that evaluates a string as a Python expression.
# I used eval() to catch a SyntaxError inside a try-except block.
# Otherwise, the code would not start executing because Python checks syntax before execution.