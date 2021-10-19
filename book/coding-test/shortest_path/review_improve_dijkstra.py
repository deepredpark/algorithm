# Review
# improve dijkstra algorithm

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
# 개선된 다익스트라 알고리즘은 힙구조를 이용하며, 방문기록 확인 X
# visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for i in range(m):
  # a(node) -> b(node), cost = c
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  
# 아래 메서드는 최소힙으로 구현
# def get_smallest_node():
#   min_distance = INF
#   index = 0
#   for i in range(1, n + 1):
#     if distance[i] < min_distance and not visited[i]:
#       min_distance = distance[i]
#       index = i
#   return index

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  # visited[start] = True
  while q:
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시(visited 역할 수행)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i])
