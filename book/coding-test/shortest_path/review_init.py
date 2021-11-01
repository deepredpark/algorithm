# Review
# shortest-path
# Dijkstra algorithm
# 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
# note! Dijkstra shortest path ps는 노드에 음의 간선이 없을 때 정상적으로 동작!

# page232
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())

# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# dp = [INF] * (n + 1)

# for _ in range(m):
#   a, b, c = map(int, input().split())
#   graph[a].append((b, c))

# def get_smallest_node():
#   min_value = INF
#   index = 0
#   for i in range(1, n + 1):
#     if not visited[i] and dp[i] < min_value:
#       index = i
#       min_value = dp[index]
#   return index

# def dijkstra(start):
#   dp[start] = 0
#   visited[start] = True
#   for i in graph[start]:
#     dp[i[0]] = i[1]
  
#   for i in range(n - 1):
#     now = get_smallest_node()
#     visited[now] = True
#     for j in graph[now]:
#       if visited[j[0]]:
#         continue
#       cost = dp[now] + j[1]
#       if dp[j[0]] > cost:
#         dp[j[0]] = cost

# dijkstra(start)

# for i in range(1, n + 1):
#   if dp[i] == 'INF':
#     print('INFINITY')
#   else:
#     print(dp[i])

# page242
# Dijkstra upgrade (using heap)
# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())

# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# dp = [INF] * (n + 1)

# for _ in range(m):
#   a, b, c = map(int, input().split())
#   graph[a].append((b, c))

# def dijkstra(start):
#   q = []
#   heapq.heappush(q, (0, start))
#   dp[start] = 0

#   while q:
#     dist, now = heapq.heappop(q)
#     if dp[now] < dist:
#       continue
#     for i in graph[now]:
#       cost = dist + i[1]
#       if cost < dp[i[0]]:
#         dp[i[0]] = cost
#         heapq.heappush(q, (cost, i[0]))

# dijkstra(start)

# for i in range(1, n + 1):
#   if dp[i] == 'INF':
#     print('INFINITY')
#   else:
#     print(dp[i])

# Floyd-Warshall algorithm
# 모든 지점에서 다른 모든지점까지의 최단경로 모두 구하기

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print('INFINITY')
    else:
      print(graph[a][b], end=' ')
  print()
