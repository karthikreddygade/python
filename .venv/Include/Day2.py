# Day 2 of 100 days of learning python
print("Welcome to the tip Calculator")
total_bill = float(input("whats your total bill?"))
tip = int(input("How much percentage of tip would you like to give?"))
persons = int(input("how many persons are there"))
tip = (tip/100)*total_bill
person_should_pay = (total_bill + tip) / persons
print(f"Each person should pay {round(person_should_pay , 2)}")
