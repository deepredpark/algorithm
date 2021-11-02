# BOJ p11657 타임머신
# Bellman-ford's algorithm
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edge = []
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  edge.append((a, b, c))

def bf(start):
  distance[start] = 0
  
  for i in range(n):
    for j in range(m):
      now = edge[j][0]
      next = edge[j][1]
      cost = edge[j][2]
      if distance[now] != INF and distance[next] > distance[now] + cost:
        distance[next] = distance[now] + cost
        if i == n - 1:
          return True
  return False

negative_cycle = bf(1)

if negative_cycle:
  print(-1)
else:
  for i in range(2, n + 1):
    if distance[i] == INF:
      print(-1)
    else:
      print(distance[i])
