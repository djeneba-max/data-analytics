# 5.
current_savings = 1000
ir = 6
year_to_double = 72/ir
doubled_balance = current_savings*2



print("Your current savings is " + str(current_savings) + ".")
print("At a " + str(ir) +"%" + " interest rate, your savings account will be")
print("worth",doubled_balance, "in", format(year_to_double, ".0f"), "years.")