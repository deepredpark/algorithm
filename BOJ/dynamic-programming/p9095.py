import sys
input = sys.stdin.readline

t = int(input())
n = []
for _ in range(t):
  n.append(int(input()))
max_n = max(n)

dp = [0] * (max_n + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
  
for j in range(4, max_n + 1):
  dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]

for i in n:
  print(dp[i])
