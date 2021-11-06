# BOJ p11057 오르막 수
n = int(input())
dp = [[1 for i in range(0, 10)] for _ in range(n + 1)]

for i in range(2, n + 1):
  dp[i][0] = dp[i - 1][0]
  for j in range(1, 10):
    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(sum(dp[n]) % 10007)
