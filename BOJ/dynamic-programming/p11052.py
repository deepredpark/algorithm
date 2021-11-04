# BOJ p11052 카드 구매하기
n = int(input())
array = [0]
array += list(map(int, input().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

dp[1][1] = array[1]

for i in range(2, n + 1):
  for j in range(1, i + 1):
    if j < i:
      dp[i][j] = dp[i - 1][j]
    if j == i:
      dp[i][j] = array[j]
      for k in range(1, (j // 2) + 1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + dp[i - 1][k])

print(dp[n][n])
