bill = float(input('What was the total bill? $'))
tip = float(input('How much tip would you like to give? 10, 12, or 15? '))
splittingTheBill = float(input('How many people to split the bill? '))

bill_per_person = (bill + bill * (tip/100)) / splittingTheBill

print(f"Each person should pay: ${round(bill_per_person, 2)}")