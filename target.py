target =int(input())
value = 0
n = 0
for n in range(2, target +1  , 2):
  if n != target: 
    
    value += n
  else:
    exit
print(value)


