# BOJ p11404 플로이드 
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = min(graph[a][b], c)

for x in range(1, n + 1):
  for y in range(1, n + 1):
    if x == y:
      graph[x][y] = 0

for k in range(1, n + 1):
  for x in range(1, n + 1):
    for y in range(1, n + 1):
      graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for x in range(1, n + 1):
  for y in range(1, n + 1):
    if graph[x][y] == INF:
      print(0, end=' ')
    else:
      print(graph[x][y], end=' ')
  print()
