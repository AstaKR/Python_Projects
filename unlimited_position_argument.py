# def sum_numbers(*args):
#     print(args)
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)

# sum_numbers(4,6,5,4)

def sum_number(n , **kwargs):
    print(kwargs)

    for (key , values) in kwargs.items():
        print(key)
        print(values)
        n += kwargs["add"]
        n *= kwargs["multiply"]
        print(n)

sum_number(5 ,add=5, multiply= 2)