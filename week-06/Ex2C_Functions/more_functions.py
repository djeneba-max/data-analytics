def display_mailing_label(name, address, city, state, zip):
    print(f"Mailing label :\n{name}\n{address}\n{city}, {state} {zip}")


def add_numbers(*numbers):   
    result = sum(numbers)    # sum() is a built-in Python function that adds all numeric elements in a sequence, such as a list or tuple.
    print(f"[{' + '.join(map(str, numbers))}] = {result}") 

# * allows a function to accept a variable number of positional arguments.
# numbers becomes a tuple that contains these arguments.
# .join() inserts the chosen separator between each element of a sequence of strings.
# map(str, numbers) converts each element of the tuple to a string before .join() combines them.


def display_receipt(total_due, amount_paid):
    if amount_paid < total_due:
        remaining_balance = total_due - amount_paid
        print(f"Total Due: ${total_due:.2f}")
        print(f"Amount Paid: ${amount_paid:.2f}")
        print(f"Remaining Balance: ${remaining_balance:.2f}")
        
    else:     
        change_due = amount_paid - total_due
        print(f"Total Due: ${total_due:.2f}")
        print(f"Amount Paid: ${amount_paid:.2f}")
        print(f"Change Due: ${change_due:.2f}")


# a)
display_mailing_label('Hamidou Ballo', '123 Leaf Street', 'New York', 'NY', 12345)
print()
display_mailing_label('Thierno Ly', '123 Snow Street', 'New Jersey ', 'NJ', 12300)
print()

# b)
add_numbers(5)
print()
add_numbers(5,2)
print()
add_numbers(3,9,6)
print()

# c)
display_receipt(50.69, 60)
print()
display_receipt(50,50)
print()
display_receipt(56.32,40)