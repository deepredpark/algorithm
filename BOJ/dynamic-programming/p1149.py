# BOJ p1149 RGB거리
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
  r, g, b = map(int, input().split())
  graph[i].extend([r, g, b])

dp = [[0, 0, 0] for _ in range(n + 1)]
dp[1] = graph[1]
for i in range(2, n + 1):
  dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + graph[i][0]
  dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + graph[i][1]
  dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][2]

print(min(dp[n]))
