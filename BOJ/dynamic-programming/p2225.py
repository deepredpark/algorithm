# BOJ 2225 합분해
# 시간 복잡도 = n * (n + 1) / 2 * k = O(K*N^2)
n, k = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(k)]
dp[0] = [1] * (n + 1)
for row in range(1, k):
  for i in range(n + 1):
    for j in range(i + 1):
      dp[row][i] += dp[row - 1][j]

print(dp[k - 1][n] % int(1e9))
