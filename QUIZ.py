# x = "hello"[0]
# print(x)
# p, q, r = 10, 20 ,30
# print(p, q, r)

# for i in range(1, 5):
#     print(i)
# else:
#     print("this is else block statement" )

# var = "James" * 2  * 3
# print(var)

# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)

# calculate(5, 6)

# valueOne = 5 ** 2
# valueTwo = 5 ** 3

# salary = 8000

# def printSalary():
#   salary = 12000
#   print("Salary:", salary)
  
# printSalary()
# print("Salary:", salary)


# print(valueOne)
# print(valueTwo)

# for i in range(10, 15, 1):
#   print( i, end=', ')

# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)

# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]

# print(listOne == listTwo)
# print(listOne is listTwo)

# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)

# var= "James Bond"
# print(var[2::-1])

# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)

# var1 = 1
# var2 = 2
# var3 = "3"

# print(var1 + var2 + var3)

# str = "pynative"
# print (str[1:3])

# for x in range(0.5, 5.5, 0.5):
#   print(x)


# print type(type(int))

# L = [\'a\',\'b\',\'c\',\'d\']
# print(\"\".join(L))

# import time

# count_seconds = 3
# for i in reversed(range(count_seconds + 1)):
#     if i > 0:
#         print(i, end='>>>', flush = True)
#         time.sleep(1)
#     else:
#         print('Start')

# a=12
# b=12
# c=2022
# print(a,b,c,sep="-")


# import io

# # declare a dummy file
# dummy_file = io.StringIO()

# # add message to the dummy file
# print('Hello Geeks!!', file=dummy_file)

# # get the value from dummy file
# print(dummy_file.getvalue())

# print("Test file for learning file in python" , file=open("kali.txt", "w"))



# For Strings
# x, y = input().split()
# print(x,y)
 
# # For integers and floating point
# # numbers
# m, n = map(int, input().split()) 
# print(m,n)
# print(type(n))
# m, n = map(float, input().split())
# print(m,n)
# print(type(n))



# Taking input from the user as list
 
# li =list(input("Enter number "))
 
# # output
# print(li)


# words_str = input("Enter a list of words, separated by spaces: ")
# words = {word: len(word) for word in words_str.split()}
# print(words)


# def number_to_the_power_of(number_one, number_two):
#         """Raise a number to an arbitrary power.

#         :param number_one: int the base number.
#         :param number_two: int the power to raise the base number to.
#         :return: int - number raised to power of second number

#         Takes number_one and raises it to the power of number_two, returning the result.
#         """

#         return number_one ** number_two

# # Calling the .__doc__ attribute of the function and printing the result.
# print(number_to_the_power_of.__doc__)

