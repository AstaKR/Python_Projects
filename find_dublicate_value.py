# from collections import Counter
# a= [1 , 5, 2 , 1 , 3 , 4 , 2,  1 , 1 , 2]
# seen = set()
# dublicate = []
# j = 0
# n = 0
# for i in a :
#         if i  in seen:
#                 dublicate.append(i)
#         else:
#                 seen.add(i)

# print(i)
# print(seen)
# print(dublicate.counter)


# my_list = Counter(a)
# print(my_list)

a= [1 , 5, 2 , 1 , 3 , 4 , 2,  1 , 1 ,1, 5, 2]
count= {}
for i in a :
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
print(count)
hightest_value = 0
for i in count:
    if count[i] >= hightest_value:
        hightest_value = count[i]
    else:
        hightest_value = count[i]
        
print(f"Highest dublicate No  is : {hightest_value} , Hightest dublicate count is {count[hightest_value]}")

# Output:
# {1: 5, 5: 2, 2: 3, 3: 1, 4: 1}
# Highest dublicate No  is : 1 , Hightest dublicate count is 5