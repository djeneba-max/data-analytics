department_code = int(input("Enter department code: "))

if department_code == 1:
    print("Marketing")
elif department_code == 5:
    print("Human Resources")
elif department_code == 10:
    print("Accounting")
elif department_code == 12:
    print("Legal")
elif department_code == 18:
    print("IT")
elif department_code == 20:
    print("Customer Relations")
else:
    print("Invalid department code")


# if/elif/else
# Python first checks the initial condition, then moves on to the next ones. 
# It stops as soon as it finds a True condition, executes the corresponding block, and ignores the remaining conditions.
# If none of the conditions are True, it executes the else block.