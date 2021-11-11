# BOJ 12865 평범한 배낭
import sys
import copy
input = sys.stdin.readline

n, k = map(int, input().split())
items = []
for _ in range(n):
  items.append(tuple(map(int, input().split())))

items.sort()

dp = [[0] * (k + 1) for _ in range(2)]
for weight, value in items:
  for j in range(1, k + 1):
    if j >= weight:
      dp[1][j] = max(dp[0][j], dp[0][j - weight] + value)
  dp[0] = copy.deepcopy(dp[1])
print(dp[1][k])
