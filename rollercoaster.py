# print("Welcome to Kali Roller Coaster")
# # Total_no_of_person = int(input("Enter the Total no of person : "))
# height = float(input("Enter your height"))
# if height <=180:
#     print("you can ride the Roller Coaster")
#     age = int(input("Enter your age: "))
#     if age <= 12 :
#         print("You pay $5")
#     elif age <= 18:
#         print("You pay $8")
#     else:
#         print("You pay $12")
# else:
#     print("Sorry!. You are not eliable to ride the Roller Coaster")



print("Welcome to Kali Roller Coaster")
# Total_no_of_person = int(input("Enter the Total no of person : "))
height = float(input("Enter your height"))
if height <=180:
    print("you can ride the Roller Coaster")
    age = int(input("Enter your age: "))
    if age <= 12 :
        bill = 5
        print("Childrens fees is  $5")
    elif age <= 18:
        bill = 8
        print("teenage fees is  $8")
    else:
        bill = 12
        print("Adults fees is $12")

    want_pic = input("Do you want picture?  Y / N ")
    if  want_pic == "y" or want_pic == "Y":
        bill += 3 
    print(f"Kindly pay Bills : {bill}")
else:
    print("Sorry!. You are not eliable to ride the Roller Coaster")









