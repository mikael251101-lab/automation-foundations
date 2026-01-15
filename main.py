monthly_income = 5_000_000
monthly_expenses = 3_500_000

savings = monthly_income - monthly_expenses

print("Monthly savings:", savings)

if savings >= 2_000_000:
    print("Excellent. You can invest.")
elif savings > 0:
    print("Good. Focus on skill building.")
else:
    print("Danger zone. Cut expenses or increase income.")
