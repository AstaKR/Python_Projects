import random
name_list  = input()
name = name_list.split(", ")
name_count = len(name)
choice = random.randint(0 ,name_count - 1)
print(f"{name[choice]} is going to buy the meal today !")


random.ra