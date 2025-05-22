monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${savings}")
annual_savings = savings * 12 + (savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${annual_savings}")