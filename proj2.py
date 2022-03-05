print("Welcome to the tip calculator!")
print("______________________________")
print("")

bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
total_bill = bill + (bill * tip)
split_num = int(input("How many people to split the bill? "))
split_pay = round(total_bill / split_num, 2)

print(f"Each person should pay: ${split_pay:.2f}")
