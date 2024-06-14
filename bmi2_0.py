height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))
bmi= (weight / height **2)
if bmi <=18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi <25 :
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi <30 :
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi <35 :
    print(f"Your BMI is {bmi}, you are obese.")
else: 
    print(f"Your BMI is {bmi}, you are clinically obese.")

# OUTPUT:
# Enter your height: 5.5
# Enter your weight: 60
# Your BMI is 1.9834710743801653, you are underweight.