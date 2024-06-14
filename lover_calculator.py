name1 = input("Enter the First Person name : ")
name2 = input("Enter the Second person name : ")
full_name = (name1 + name2).lower()
t = full_name.count("t")
u = full_name.count("u")
r = full_name.count("r")
e = full_name.count("e")
output1 = t + u + r + e
l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
e = full_name.count("e")
output2 = l + o + v + e
final_output = int(str(output1) + str(output2))
if final_output <=10 or final_output >=90:
    print(f"Your score is {final_output}, you go together like coke and mentos.")
elif final_output > 40 and final_output <50 :
    print(f"Your Score is {final_output}, you are alright together.")
else:
    print(f"Your score is {final_output}.")