# Review
# Dynamic programming

# Recurrence relation - express the recursive function
# a(n+2) = a(n+1) + a(n) (a(1) , a(2) = 1, n >= 1)
# def fibo(n):
#   if n == 1 or n == 2:
#     return 1
#   return fibo(n - 1) + fibo(n - 2)

# Arithmatic sequence
# a(n+1) = a(n) + 1 (a(1) = 1, n >= 1)
def AP(n):
  if n == 1:
    return 1
  return AP(n-1) + 1

# Geometric sequence
# a(n+1) = a(n) * 3 (a(1) = 1, n >= 1)
def GP(n):
  if n == 1:
    return 1
  return GP(n - 1) * 3

# DP1 - memoization(cashing)
# Top-Down
DP = [0] * 101

def fibo(n):
  print('f(' + str(n) + ')', end=' ')
  if n == 1 or n == 2:
    return 1
  if DP[n] != 0:
    return DP[n]
  
  DP[n] = fibo(n - 1) + fibo(n - 2)
  return DP[n]

# DP2
# Bottom-Up
DP2 = [0] * 101

DP[1] = 1
DP[2] = 1
n = 100

for i in range(3, n + 1):
  DP[i] = DP[i - 1] + DP[i - 2]

print(DP[n])
