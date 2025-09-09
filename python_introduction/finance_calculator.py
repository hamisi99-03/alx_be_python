monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)
print("Your monthly savings are $", str(int(monthly_savings)) + ".")
print("Projected savings after one year, with interest, is:$", str(int(projected_annual_savings)) + ".")
