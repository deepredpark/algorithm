# Review 1
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())

# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# distance = [INF] * (n + 1)

# for _ in range(m):
#   a, b, c = map(int, input().split())
#   graph[a].append((b, c))

# def get_smallest_node():
#   min_value = INF
#   index = 0
#   for i in range(1, n + 1):
#     if not visited[i] and distance[i] < min_value:
#       index = i
#       min_value = distance[index]
#   return index

# def dijkstra(start):
#   distance[start] = 0
#   visited[start] = True
#   for i in graph[start]:
#     distance[i[0]] = i[1]
  
#   for i in range(n - 1):
#     now = get_smallest_node()
#     visited[now] = True
#     for j in graph[now]:
#       cost = distance[now] + j[1]
#       if distance[j[0]] > cost:
#         distance[j[0]] = cost

# dijkstra(start)

# for i in range(1, n + 1):
#   if distance[i] == INF:
#     print('INFINITY')
#   else:
#     print(distance[i])

# review2. upgrade dijkstra

# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)
# for _ in range(m):
#   a, b, c, = map(int, input().split())
#   graph[a].append((b, c))

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

# Review 3. Floyd-Warshall
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
  for y in range(1, n + 1):
    if x == y:
      graph[x][y] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

for k in range(1, n + 1):
  for x in range(1, n + 1):
    for y in range(1, n + 1):
      graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for x in range(1, n + 1):
  for y in range(1, n + 1):
    if graph[x][y] == INF:
      print('INFINITY', end=' ')
    else:
      print(graph[x][y], end=' ')
  print()
