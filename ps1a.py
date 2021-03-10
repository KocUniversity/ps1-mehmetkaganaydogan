n, B = list(map(int, input().strip().split()))
T = 0

# your code here
sum = 0
while sum * T <= B :
  for x in range(1, n+1):
    if x % 2 == 0 :
      p = 2**x + 1
    else :
      p = 3**x + 1
    sum += p**(n-1)
    n -= 1
  T += 1
  if T > 10000 :
    T = -1
    break

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)