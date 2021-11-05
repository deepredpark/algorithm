# Review 4
# Dijkstra(simple, upgrade), Floyd-Warshall, Bellman-Ford
# 1. Dijkstra(simple) - using list O(V^2)
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#   a, b, c = map(int, input().split())
#   graph[a].append((b, c))
# visited = [False] * (n + 1)
# distance = [INF] * (n + 1)

# def get_smallest_node():
#   min_value = INF
#   index = 0
#   for i in range(n):
#     if not visited[i] and distance[i] < min_value:
#       index = i
#       min_value = distance[i]
#   return index

# def dijkstra(start):
#   visited[start] = True
#   distance[start] = 0
#   for i in graph[start]:
#     distance[i[0]] = i[1]
  
#   for i in range(n - 1):
#     now = get_smallest_node()
#     visited[now] = True
#     for j in graph[now]:
#       cost = distance[now] + j[1]
#       if cost < distance[j[0]]:
#         distance[j[0]] = cost

# dijkstra(start)

# for i in range(1, n + 1):
#   if distance[i] == INF:
#     print('INFINITY')
#   else:
#     print(distance[i])

# 2. Dijkstra(upgrade) - using heapq O(ElogV)
# import sys
# import heapq

# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#   a, b, c = map(int, input().split())
#   graph[a].append((b, c))
# distance = [INF] * (n + 1)

# def dijkstra(start):
#   q = []
#   heapq.heappush(q, (0, start))
#   distance[start] = 0
#   while q:
#     dist, now = heapq.heappop(q)
#     if dist > distance[now]:
#       continue
#     for i in graph[now]:
#       cost = dist + i[1]
#       if cost < distance[i[0]]:
#         distance[i[0]] = cost
#         heapq.heappush(q, (cost, i[0]))

# dijkstra(start)

# for i in range(1, n + 1):
#   if distance[i] == INF:
#     print('INFINITY')
#   else:
#     print(distance[i])

# 3. Floyd-Warshall - O(V^3)
# import sys

# input = sys.stdin.readline
# INF = int(1e9)

# n = int(input())
# m = int(input())

# graph = [[INF] * (n + 1) for _ in range(n + 1)]
# for _ in range(m):
#   x, y, cost = map(int, input().split())
#   graph[x][y] = cost

# for x in range(1, n + 1):
#   for y in range(1, n + 1):
#     if x == y:
#       graph[x][y] = 0

# for k in range(1, n + 1):
#   for x in range(1, n + 1):
#     for y in range(1, n + 1):
#       graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

# for x in range(1, n + 1):
#   for y in range(1, n + 1):
#     if graph[x][y] == INF:
#       print('INFINITY', end=' ')
#     else:
#       print(graph[x][y], end=' ')
#   print()

# 4. Bellman-Ford - O(VE)
# import sys

# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# edge = []
# for _ in range(m):
#   a, b, c = map(int, input().split())
#   edge.append((a, b, c))
# distance = [INF] * (n + 1)

# def bf(start):
#   distance[start] = 0
#   for i in range(n):
#     for j in range(m):
#       now, next, cost = edge[j]
#       if distance[now] != INF and distance[now] + cost < distance[next]:
#         distance[next] = distance[now] + cost
#         if i == n - 1:
#           return True
#   return False

# negative_cycle = bf(1)

# if negative_cycle:
#   print(-1)
# else:
#   for i in range(2, n + 1):
#     if distance[i] == INF:
#       print('INFINITY')
#     else:
#       print(distance[i])


