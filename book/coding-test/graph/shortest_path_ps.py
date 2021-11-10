# 미래도시 page259
# import sys

# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
# for _ in range(m):
#   a, b = map(int, input().split())
#   graph[a][b] = graph[b][a] = 1
# for x in range(1, n + 1):
#   for y in range(1, n + 1):
#     if x == y:
#       graph[x][y] = 0

# for k in range(1, n + 1):
#   for x in range(1, n + 1):
#     for y in range(1, n + 1):
#       graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

# X, K = map(int, input().split())
# if graph[1][K] == INF or graph[K][X] == INF:
#   print(-1)
# else:
#   print(graph[1][K] + graph[K][X])

# 전보 page262
# import sys
# import heapq

# input = sys.stdin.readline
# INF = int(1e9)

# n, m, start = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#   s, e, time = map(int, input().split())
#   graph[s].append((e, time))
# times = [INF] * (n + 1)

# def dijkstra(start):
#   q = []
#   heapq.heappush(q, (0, start))
#   times[start] = 0
#   while q:
#     time, now = heapq.heappop(q)
#     if time > times[now]:
#       continue
#     for i in graph[now]:
#       cost = time + i[1]
#       if cost < times[i[0]]:
#         times[i[0]] = cost
#         heapq.heappush(q, (cost, i[0]))

# dijkstra(start)

# cities = 0
# max_time = 0
# for i in range(1, n + 1):
#   if times[i] != INF:
#     cities += 1
#     if times[i] > max_time:
#       max_time = times[i]
# print(cities - 1, max_time)

# BOJ p11657 타임머신
# Bellman-Ford's algorithm - O(VE)
# import sys

# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# edges = []
# for _ in range(m):
#   a, b, c = map(int, input().split())
#   edges.append((a, b, c))
# distance = [INF] * (n + 1)

# def bellman(start):
#   distance[start] = 0
#   for i in range(n):
#     for edge in edges:
#       now, next, dist = edge
#       if distance[now] != INF and distance[now] + dist < distance[next]:
#         distance[next] = distance[now] + dist
#         if i == n - 1:
#           return True
#   return False

# negative_cycle = bellman(1)
# if negative_cycle:
#   print(-1)
# else:
#   for i in range(2, n + 1):
#     if distance[i] >= INF:
#       print(-1)
#     else:
#       print(distance[i])

# BOJ p1865 웜홀 (upgrade bellman)
# Bellman-Ford's algorithm - O(T * V * E)
# negative_cycle
# import sys
# input = sys.stdin.readline
# INF = 100001

# def bellman(start):
#   distance[start] = 0
#   for i in range(n):
#     for edge in edges:
#       now, next, dist = edge
#       if distance[now] + dist < distance[next]:
#         distance[next] = distance[now] + dist
#         if i == n - 1:
#           return True
#   return False

# t = int(input())
# for _ in range(t):
#   n, m, w = map(int, input().split())
#   edges = []
#   for _ in range(m):
#     s, e, t = map(int, input().split())
#     edges.append((s, e, t))
#     edges.append((e, s, t))
#   for _ in range(w):
#     s, e, t = map(int, input().split())
#     edges.append((s, e, -t))
#   distance = [INF] * (n + 1)

#   negative_cycle = bellman(1)
#   if negative_cycle:
#     print('YES')
#   else:
#     print('NO')
