# Variables

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# Using .lower() to convert all three names to lowercase
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Using Use .title() to convert all three names to title case
print(name_1.title())
print(name_2.title())
print(name_3.title())

# Using .replace() to remove the $ from both salary strings
print(salary_1.replace('$',''))
print(salary_2.replace('$',''))

print(type(salary_1.replace('$','')))
print(type(salary_2.replace('$','')))

# Remove the comma as well, then convert the strings 
# to floats so we can perform mathematical operations on the variables.
salary1 =float(salary_1.replace('$','').replace(',',''))
salary2 =float(salary_2.replace('$','').replace(',',''))
print(salary1, type(salary1))
print(salary2, type(salary2))

# Chain .replace() and int
salary1_int =int(salary_1.replace('$','').replace(',',''))
salary2_int =int(salary_2.replace('$','').replace(',',''))
print(salary1_int, type(salary1_int))
print(salary2_int, type(salary2_int))
# I noticed that I had already almost answered this question in the previous one.