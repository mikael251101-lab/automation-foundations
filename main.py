#cash
monthly_income = 5_000_000
monthly_expenses = 3_500_000
monthly_savings = monthly_income - monthly_expenses

print('Monthly savings:', monthly_savings)

if monthly_savings >= 2_000_000:
    print('You are ready to invest')
elif monthly_savings > 0:
    print('Focus on skills building')
else: 
    print('Warning: financial risk')

months = 6
total_savings = 0

#investments
investment_balance = 0
investment_rate = 0.05   # 5% per month
investment_ratio = 0.30  # 30% of savings
cash_savings = 0

for month in range (1, 1 + months):
    current_expenses = monthly_expenses
    if month == 4:
        monthly_income += 500_000
        print('Month 4: Income increased!')
    if month == 5:
        current_expenses += 1_000_000
        print('Month 5: Emergency expense')
    
    monthly_savings = monthly_income - current_expenses
    total_savings += monthly_savings

    if month >= 4:
        invest_amount = monthly_savings * investment_ratio
        cash_amount = monthly_savings - invest_amount
    else:
        invest_amount = 0
        cash_amount = monthly_savings
    
    cash_savings += cash_amount
    investment_balance += invest_amount
    investment_balance *= (1 + investment_rate)
    total_net_worth = cash_savings + investment_balance

    print('Month', month)
    print(' Cash savings:', cash_savings)
    print(' Investment balance:', investment_balance)
    print(' Net worth:', int(total_net_worth))