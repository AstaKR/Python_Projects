print("Thank you for choosing Python Pizza Deliveries!")
size = input(" What size pizza do you want? S, M, or L  :") 
add_pepperoni = input("Do you want pepperoni? Y or N  :") 
extra_cheese = input("Do you want extra cheese? Y or N  :") 
cash = 0
if size == "S" or size == "s" :
  cash += 15
elif size == "M" or size == "m" :
  cash += 20
else:
   cash += 25
if add_pepperoni == "Y" or add_pepperoni == "y":
  if size == "S" or size == "s":
    cash += 2
  else:
    cash += 3
if extra_cheese == "Y" or extra_cheese == "y":
  cash += 1
print(f"Your final bill is: ${cash}.")


