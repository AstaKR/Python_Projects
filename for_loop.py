max_value = int(input("Enter the  maximum value:" ))
total = 0 
for n in range ( 2, max_value + 1, 2 ):
    print(n)
    total += n 
print(total)