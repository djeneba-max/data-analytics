# Test 1
pay_rate = 12.50
hours_worked = 20

if hours_worked > 40: 
    regular_pay = 40 * pay_rate
    overtime = hours_worked - 40
    overtime_pay = overtime * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
    print(f'Gross pay is: ${gross_pay:.2f}')
else: 
    gross_pay = hours_worked * pay_rate
    print(f'Gross pay is: ${gross_pay:.2f}')


# Test 2
pay_rate = 25.50
hours_worked = 40

if hours_worked > 40: 
    regular_pay = 40 * pay_rate
    overtime = hours_worked - 40
    overtime_pay = overtime * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
    print(f'Gross pay is: ${gross_pay:.2f}')
else: 
    gross_pay = hours_worked * pay_rate
    print(f'Gross pay is: ${gross_pay:.2f}')

# Test 3
pay_rate = 17.30
hours_worked = 45

if hours_worked > 40: 
    regular_pay = 40 * pay_rate
    overtime = hours_worked - 40
    overtime_pay = overtime * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
    print(f'Gross pay is: ${gross_pay:.2f}')
else: 
    gross_pay = hours_worked * pay_rate
    print(f'Gross pay is: ${gross_pay:.2f}')

# I kept the different test values in the script to get a better 
# overall understanding of the outputs and how the conditions work.