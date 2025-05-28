print("Welcome to the tip Calculator!")
bill=float(input("What was the total Bill? $"))
tip=int(input("How much percentage tip would you like to give 10, 12, 15? "))
people=int(input("How much people you want to split the Bill: "))
tip_amount=(tip/100)*bill
total_bill=tip_amount+bill
final_amount=round(total_bill/people,2)
print(f"Each person should pay: ${final_amount}")
