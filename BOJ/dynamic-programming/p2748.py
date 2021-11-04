# BOJ p2748 피보나치 수 2
n = int(input())

dp = [0] * (n + 1)
if n == 1:
  print(1)
else:
  dp[1] = 1
  for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
  print(dp[n])
