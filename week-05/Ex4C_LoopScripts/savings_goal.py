bank_balance = 50
savings_goal = 20_000
weekly_savings = 500
treat_cost = 50


while bank_balance < savings_goal:
    bank_balance += weekly_savings

    if bank_balance >= savings_goal:
        break    # break prevents two messages from being displayed when the balance reaches or exceeds the savings goal.
    
    elif bank_balance >= savings_goal * 0.75:
        bank_balance -= treat_cost
        print(f'So close! After treating myself, my balance is up to ${bank_balance}.')
    
    elif bank_balance > savings_goal / 2:
        print(f'Almost there! This week my balance is up to ${bank_balance}.')
    
    else:
        print(f'This week my balance increased to ${bank_balance}.')
   
    
print(f'Goal met! My current balance is ${bank_balance}.')

