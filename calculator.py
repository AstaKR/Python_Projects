def add(num1 , num2):
  return num1 + num2
def sub(num1 , num2):
  return num1 - num2
def mul(num1 , num2):
  return num1 * num2
def div(num1 , num2):
  return num1 / num2
functional_opeartion = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}
def calculator():       
    num1 = int(input("Enter the number 1 value :"))
    i = True
    while i == True:
      for key in functional_opeartion:
            print(key)  
      operation = input("Select the any opeation above :")
      num2 = int(input("Enter the number 2 value :"))
      function_operator = functional_opeartion[operation] 
      answer = function_operator(num1, num2)
      print(f"Result is : {num1} {operation} {num2} : {answer}")
      option = input("Do you want contiune type y or exit Type q or Start the New start type n :").lower()
      if option == "y":
          num1 = answer
      elif option == "n":
          i = False
          calculator()
      else:
          i = False         
calculator()



# Output:
# Enter the number 1 value :15
# +
# -
# *
# /
# Select the any opeation above :+
# Enter the number 2 value :5
# Result is : 15 + 5 : 20
# Do you want contiune type y or exit Type q or Start the New start type n :y
# +
# -
# *
# /
# Select the any opeation above :-
# Enter the number 2 value :5
# Result is : 20 - 5 : 15
# Do you want contiune type y or exit Type q or Start the New start type n :n
# Enter the number 1 value :25 
# +
# -
# *
# /
# Select the any opeation above :+
# Enter the number 2 value :25
# Result is : 25 + 25 : 50
# Do you want contiune type y or exit Type q or Start the New start type n :q