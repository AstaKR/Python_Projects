print("Welcome to Tip Calculator")
bill_amount = float(input("Kindly Enter the Bill Amount: $"))
tip_amount= int(input("How much tip would you like to give? 10, 12, or 15"))
peoples = int(input("How many people to split the bills?"))
pay_amount = round((((tip_amount /100)* bill_amount)+ bill_amount) / peoples , 2) # ,2 for 2 demical value for round 
pay_amount = "{:.2f}".format(pay_amount)
print(f"Each person should pay:$ {pay_amount}")
# Output:
# Welcome to Tip Calculator
# Kindly Enter the Bill Amount: $150
# How much tip would you like to give? 10, 12, or 1510
# How many people to split the bills?5
# Each person should pay:$ 33.00