monthlyIncome = int(input('Enter monthly income: '))
monthlyExpenses = int(input('Enter total expenses: '))

monthlySavings = monthlyIncome - monthlyExpenses

projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

print (f'Your monthly savings are ${monthlySavings}.')
print (f'Projected saving after one year, with interest, is: ${projectedSavings}.')