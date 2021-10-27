# reference : https://myjamong.tistory.com/317

# additional algorithm (LCS)
# 최장 공통 부분수열(Longest common subsequence)
# BOJ p9251 LCS
a = input()
b = input()
n = len(a)
m = len(b)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, m + 1):
    if a[i - 1] == b[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
