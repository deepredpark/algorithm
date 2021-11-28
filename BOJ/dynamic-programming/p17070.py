# BOJ 17070 파이프 옮기기
# reference = https://pacific-ocean.tistory.com/458 (dp 구현하는 idea)
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
# 가로로 갈 수 있는 첫 줄 경우의 수
for i in range(2, n):
  if graph[0][i] == 0:
    dp[0][0][i] = dp[0][0][i - 1]
# 점화식
# a[0][i][j] (가로로 i, j 위치로 갈 수 있는 경우의 수) = a[0][i][j - 1] + a[2][i][j - 1]
# a[1][i][j] (세로로 i, j 위치로 갈 수 있는 경우의 수) = a[1][i - 1][j] + a[2][i - 1][j]
# a[0][i][j] (대각선으로 i, j 위치로 갈 수 있는 경우의 수) = a[0][i - 1][j - 1] + a[1][i - 1][j - 1] + a[2][i - 1][j - 1]

for i in range(1, n):
  for j in range(2, n):
    if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
      dp[2][i][j] = dp[0][i - 1][j - 1]  + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
    if graph[i][j] == 0:
      dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
      dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
print(dp[0][n -1][n - 1] + dp[1][n -1][n - 1] + dp[2][n -1][n - 1])
