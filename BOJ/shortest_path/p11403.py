# BOJ p11403 경로 찾기
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

for k in range(n):
  for x in range(n):
    for y in range(n):
      if graph[x][k] + graph[k][y] == 2:
        graph[x][y] = 1

for x in range(n):
  for y in range(n):
    print(graph[x][y], end=' ')
  print()
