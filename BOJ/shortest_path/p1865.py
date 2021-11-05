# BOJ p1865 웜홀 
import sys

input = sys.stdin.readline
INF = 10001

def bf(start):
  distance[start] = 0
  for i in range(n):
    for j in range(len(edge)):
      now, next, cost = edge[j]
      if distance[now] + cost < distance[next]:
        distance[next] = distance[now] + cost
        if i == n - 1:
          return True
  return False

t = int(input())
for _ in range(t):
  n, m, w = map(int, input().split())
  edge = []
  for _ in range(m):
    s, e, t = map(int, input().split())
    edge.append((s, e, t))
    edge.append((e, s, t))
  for _ in range(w):
    s, e, t = map(int, input().split())
    edge.append((s, e, -t))
    
  distance = [INF] * (n + 1)

  negative_cycle = bf(1)
  if negative_cycle:
    print('YES')
  else:
    print('NO')
