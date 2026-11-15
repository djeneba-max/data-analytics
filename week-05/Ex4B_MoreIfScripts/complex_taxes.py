# Collect user information
pay_rate = float(input('Enter your hourly pay rate: $'))
hours_worked = float(input('Enter hours worked per week: '))
filing_status = input("Enter your filing status (single or joint): ").lower()


# Calculate weekly gross pay
if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime = hours_worked - 40
    overtime_pay = overtime * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate


# Calculate annual gross pay (52 weeks in a year)
annual_gross_pay = gross_pay * 52


# Determine tax rate based on filing status and annual gross pay
if filing_status == 'single':
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif annual_gross_pay < 25000:
        tax_rate = 0.10
    elif annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == 'joint':
    if annual_gross_pay < 12000:
        tax_rate = 0.00
    elif annual_gross_pay < 25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

else:
    print('Invalid filing_status')
    exit()

# Calculate weekly tax withheld
tax_withheld = gross_pay * tax_rate

# Calculate weekly net pay
net_pay = gross_pay - tax_withheld


# Display user information
print('\nYour information')
print(f'Weekly work hours: {hours_worked}')
print(f'Pay rate: ${pay_rate:.2f}/hour')
print(f'Filing status: {filing_status}')

# Calculations
print('\nCalculations')
print(f'Weekly gross pay: ${gross_pay:.2f}')
print(f'Annual gross pay: ${annual_gross_pay:.2f}')
print(f'Tax rate: {tax_rate:.0%}')
print(f'Weekly tax withheld: ${tax_withheld:.2f}')
print(f'Weekly net pay: ${net_pay:.2f}')