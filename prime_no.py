def prime_checher(n):
    is_prime = False
    for i in range(2, n):
        if n % i == 0:
            is_prime = True
    
    if is_prime:
          print(f"This {n}  is not Prime")
    else:
            print(f"This {n} is a prime ")


n = int(input("Enter the number:"))
prime_checher(n)
