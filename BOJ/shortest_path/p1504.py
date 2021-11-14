# BOJ 1504 특정한 최단 경로
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, target, graph):
  distance = [INF] * len(graph)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (distance[i[0]], i[0]))
  if distance[target] >= INF:
    return -1
  else:
    return distance[target]

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, cost = map(int, input().split())
  graph[a].append((b, cost))
  graph[b].append((a, cost))
target1, target2 = map(int, input().split())

paths = [(1, target1), (target1, target2), (target2, n)]
result1 = 0
for path in paths:
  start, target = path
  shortest_path = dijkstra(start, target, graph)
  if shortest_path == -1:
    result1 = -1
    break
  else:
    result1 += shortest_path

paths = [(1, target2), (target2, target1), (target1, n)]
result2 = 0
for path in paths:
  start, target = path
  shortest_path = dijkstra(start, target, graph)
  if shortest_path == -1:
    result2 = -1
    break
  else:
    result2 += shortest_path

if result1 == -1:
  print(result1)
else:
  print(min(result1, result2))
