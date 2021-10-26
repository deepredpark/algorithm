# Review
# Dynamic programming
# TOP-down
# DP = [0] * 10001

# def fibo(n):
#   print('fibo(',n,')')
#   if n == 1 or n == 2:
#     return 1
#   if DP[n] != 0:
#     return DP[n]
  
#   DP[n] = fibo(n - 1) + fibo(n - 2)
#   return DP[n]

# print(fibo(6))
# Bottom-up
# a(n) = a(n - 1) + a(n - 2) (n >= 3, a(1) = 1, a(2) = 1)
# dp = [0] * 10001

# dp[1] = 1
# dp[2] = 1

# n = int(input())
# for i in range(3, n + 1):
#   dp[i] = dp[i - 1] + dp[i - 2]

# print(dp[n])

# page217 1로 만들기 15min
# from collections import deque

# n = int(input())
# dp = [0] * 30001

# queue = deque()
# queue.append(n)

# while queue:
#   v = queue.popleft()
#   next = []
#   if v % 5 == 0:
#     next.append(v // 5)
#   if v % 3 == 0:
#     next.append(v // 3)
#   if v % 2 == 0:
#     next.append(v // 2)
#   next.append(v - 1)
#   for i in next:
#     if dp[i] == 0 and i >= 1:
#       dp[i] = dp[v] + 1
#       queue.append(i)
  
# print(dp[1])

# solution 2
# n = int(input())
# # a(n) = min(a(n // 5), a(n // 3), a(n // 2), a(n - 1)) + 1
# dp = [0] * 30001
# for i in range(2, n + 1):
#   dp[i] = dp[i - 1] + 1
#   if i % 5 == 0:
#     dp[i] = min(dp[i], dp[i // 5] + 1)
#   if i % 3 == 0:
#     dp[i] = min(dp[i], dp[i // 3] + 1)
#   if i % 2 == 0:
#     dp[i] = min(dp[i], dp[i // 2] + 1)

# print(dp[1:n + 1])

# page220 개미전사 8min
# n = int(input())
# array = list(map(int, input().split()))
# dp = [0] * 101
# dp[1] = array[0]
# dp[2] = max(array[0], array[1])

# for i in range(3, n + 1):
#   dp[i] = max(dp[i - 2] + array[i - 1], dp[i - 1])

# print(dp[n])
