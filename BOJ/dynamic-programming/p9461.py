# BOJ p9461 파도반 수열
import sys
input = sys.stdin.readline

t = int(input())
n = []
for _ in range(t):
  n.append(int(input()))

dp = [0] * 101
dp[1:6] = [1,1,1,2,2]
for i in range(6, 101):
  dp[i] = dp[i - 1] + dp[i - 5]

for i in n:
  print(dp[i])
