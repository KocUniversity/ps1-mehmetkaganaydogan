n, B = list(map(int, input().strip().split()))
T = 0

# your code here
high = 10000
low = 0
guess = (high + low)/2
epsilon = 0.0001
sum = 0
a = 0

for x in range(1, n+1):
  if x % 2 == 0 :
    p = 2**x + 1
  else :
    p = 3**x + 1
  sum += p**(n-1)
  n -= 1

while abs(sum * guess - B) >= epsilon :
  if sum * guess > B :
    high = guess
  elif sum * guess < B :
    low = guess
  guess = (high + low)/2

  # log2 (10000) is between 13 and 14, so we should solve this system in at most 14 loops. So, if we can't solve the system at that many tries, than we can understand that T is not in the interval that we are searching for.
  a += 1
  if a == 15 :
    break

T = int(guess) + 1

if T >= 10000 :
 T = -1

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)