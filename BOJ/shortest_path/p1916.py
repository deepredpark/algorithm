# BOJ p1916 최소비용
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
distance = [INF] * (n + 1)

start, end = map(int, input().split())

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

print(distance[end])
