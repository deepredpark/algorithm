# BOJ p1753 최단경로
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))
distance = [INF] * (n + 1)

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
  dist, now = heapq.heappop(q)
  if dist > distance[now]:
    continue
  for i in graph[now]:
    if dist != INF and dist + i[1] < distance[i[0]]:
      distance[i[0]] = dist + i[1]
      heapq.heappush(q, (distance[i[0]], i[0]))

for i in range(1, n + 1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])
