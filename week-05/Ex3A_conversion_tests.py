# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '


# Variable a = " 101.1 "
# Transformation 1: a) Cast as integer using int()
# a_1 = int(a) # ValueError: invalid literal for int() with base 10: ' 101.1 '

# Transformation 2: b) Cast as float using float()
a_2 = float(a)
print(a_2, type(a_2)) 

# Transformation 3: c) For variable a, try casting into a float then integer, like this: int(float(a))
a_3  = int(float(a)) # Converting to float first allows the string to be converted to an integer.
print(a_3, type(a_3)) 

# Transformation 4: d) Use slicing and cast the number as an integer or string
a_4 = int(float(a[1:6]))
print(a_4, type(a_4))

# Use the .strip() method
print(a.strip())



# Variable b = '55'
# Transformation 1: a) Cast as integer using int()
b_1 = int(b) 
print(b_1, type(b_1))

# Transformation 2: b) Cast as float using float()
b_2 = float(b)
print(b_2, type(b_2))

# Transformation 3: d) Use slicing and cast the number as an integer or string
b_3 = int(b[:])
print(b_3, type(b_3))



# Variable c = "402 Stevens"
# Transformation 1: a) Cast as integer using int()
# c_1 = int(c) # ValueError: invalid literal for int() with base 10: '402 Stevens'

# Transformation 2: b) Cast as float using float()
# c_2 = float(c) # ValueError: could not convert string to float: '402 Stevens'

# Transformation 3: d) Use slicing and cast the number as an integer or string
c_3 = str(c[:3])
print(c_3, type(c_3))



# Variable d = 'Number 5 '
# Transformation 1: a) Cast as integer using int()
# d_1 = int(d) # ValueError: invalid literal for int() with base 10: 'Number 5 '

# Transformation 2: b) Cast as float using float()
# d_2 = float(d) # ValueError: could not convert string to float: 'Number 5 '

# Transformation 3: d) Use slicing and cast the number as an integer or string
d_3 = str(d[7])
print(d_3, type(d_3))

# Use the .strip() method
print(d.strip())