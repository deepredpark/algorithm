# ★ graph
##############################################################################

# 1. graph representation(adjacency list, adjacency matrix)
# 2. graph search(DFS, BFS = depth first search, breadth first search)
# 3. graph-traversal(pre-order, in-order, post-order)
# 4. shortest-path(dijkstra(simple, upgrade), floyd-warshall, bellman-ford))
# 5. union-find set → MST(minimum spanning tree) (kruskal)
# 6. topological-sort
# 7. LCA(lowest common ancestor) + upgrade version
# appendix

##############################################################################
# appendix
# 1) Stack(LIFO), Queue(FIFO) - function(append, pop) + (overflow, underflow)
# (1) Stack
# stack = []
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()
# (2) Queue
# from collections import deque # collections.deque library is faster than queue library
# queue = deque()
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()
# queue.reverse()
# print(queue)
# 2) recursive-function
# def recursive_funcion(i):
#     if i == 0:
#         return
#     print('recall {0} function'. format(i))
#     recursive_funcion(i - 1)
#     print('end {0} function'. format(i))
# recursive_funcion(100)
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))
# def factorial2(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
# print(factorial2(5))
# def GCD(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return GCD(b, a % b)
# print(GCD(192, 162))
##############################################################################
# 1. graph representation(adjacency list, adjacency matrix)
# input
# 3 2 (the number of node, edge)
# 0 1 7 (undirected edge, start end weight)
# 0 2 5
# 1) adjacency matrix
# INF = int(1e9)
# n, m = map(int, input().split())
# graph = [[INF] * n for _ in range(n)]
# for x in range(n):
#     for y in range(n):
#         if x == y:
#             graph[x][y] = 0
# for _ in range(m):
#     a, b, weight = map(int, input().split())
#     graph[a][b] = graph[b][a] = weight
#
# for x in range(n):
#     for y in range(n):
#         print(graph[x][y], end=' ')
#     print()
# 2) adjacency graph
# INF = int(1e9)
# n, m = map(int, input().split())
# graph = [[] for _ in range(n)]
#
# for _ in range(m):
#     a, b, weight = map(int, input().split())
#     graph[a].append((b, weight))
#     graph[b].append((a, weight))
#
# for i in range(n):
#     print(graph[i])
##############################################################################
# 2. graph search(DFS, BFS = depth first search, breadth first search)
# page 137 input
# input
# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# visited = [False] * (n + 1)
# for i in graph[1:]:
# 1) DFS(Depth-First-Search) - O(N)
# def dfs(start):
#     visited[start] = True
#     print(start, end=' ')
#     for i in sorted(graph[start]):
#         if not visited[i]:
#             dfs(i)
# dfs(1)
# 2) BFS(Breadth-First-Search) - O(N)
# from collections import deque
# def bfs(start):
#     q = deque()
#     q.append(start)
#     visited[start] = True
#     while q:
#         now = q.popleft()
#         print(now, end=' ')
#         for i in sorted(graph[now]):
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True
# bfs(1)
##############################################################################
# 3. graph-traversal(pre-order, in-order, post-order)
##############################################################################
# 4. shortest-path(dijkstra(simple, upgrade), floyd-warshall, bellman-ford))
# 1) dijkstra(simple version) - O(N^2)
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# distance = [INF] * (n + 1)
# for _ in range(m):
#   a, b, cost = map(int, input().split())
#   graph[a].append((b, cost))
#
# def get_smallest_node():
#   min_value = INF
#   index = 0
#   for i in range(1, n + 1):
#     if not visited[i] and distance[i] < min_value:
#       index = i
#       min_value = distance[i]
#   return index
#
# def dijkstra(start):
#   visited[start] = True
#   distance[start] = 0
#   for i in graph[start]:
#     distance[i[0]] = i[1]
#   for _ in range(n - 1):
#     now = get_smallest_node()
#     visited[now] = True
#     for j in graph[now]:
#       cost = distance[now] + j[1]
#       if not visited[j[0]] and cost < distance[j[0]]:
#         distance[j[0]] = cost
#
# dijkstra(start)
# for i in range(1, n + 1):
#   print(distance[i])
# 2) dijkstra(upgrade version) - O(ElogE -> ElogV)
# import sys
# import heapq
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)
# for _ in range(m):
#   a, b, cost = map(int, input().split())
#   graph[a].append((b, cost))
#
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
#
# dijkstra(start)
#
# for i in range(1, n + 1):
#   if distance[i] == INF:
#     print('INFINITY')
#   else:
#     print(distance[i])
# 3) Floyd-Warshall algorithm - O(N^3)
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# n = int(input())
# m = int(input())
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
#
# for _ in range(m):
#   a, b, c = map(int, input().split())
#   graph[a][b] = c
#
# for x in range(1, n + 1):
#   for y in range(1, n + 1):
#     if x == y:
#       graph[x][y] = 0
#
# for k in range(1, n + 1):
#   for x in range(1, n + 1):
#     for y in range(1, n + 1):
#       graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])
#
# for x in range(1, n + 1):
#   for y in range(1, n + 1):
#     if graph[x][y] == INF:
#       print('INFINITY', end=' ')
#     else:
#       print(graph[x][y], end=' ')
#   print()
# 4) Bellman-Ford's algorithm - O(VE)
# BOJ p11657 타임머신
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

# Bellman-Ford's algorithm - O(T * V * E)
# BOJ p1865 웜홀 (upgrade bellman)
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
##############################################################################
# 5. union-find set → MST(minimum spanning tree) (kruskal)
# 1) union-find set + cycle finding
# Union-Find set
# import sys
# input = sys.stdin.readline
#
# def find_parent(parent, x):
#   if parent[x] != x:
#     parent[x] = find_parent(parent, parent[x])
#   return parent[x]
#
# def union_parent(parent, a, b):
#   a = find_parent(parent, a)
#   b = find_parent(parent, b)
#   if a < b:
#     parent[b] = a
#   else:
#     parent[a] = b
#
# n, m = map(int, input().split())
# parent = [0] * (n + 1)
# for i in range(1, n + 1):
#   parent[i] = i
#
# cycle = False
# for _ in range(m):
#   a, b = map(int, input().split())
#   if find_parent(parent, a) == find_parent(parent, b):
#     cycle = True
#     break
#   else:
#     union_parent(parent, a, b)
#
# if cycle:
#   print('사이클이 발생했습니다.')
# else:
#   print('사이클이 발생하지 않았습니다.')
# 2) Kruskal algorithm - O(ElogE)
# import sys
# input = sys.stdin.readline
#
# def find_parent(parent, x):
#   if parent[x] != x:
#     parent[x] = find_parent(parent, parent[x])
#   return parent[x]
#
# def union_parent(parent, a, b):
#   a = find_parent(parent, a)
#   b = find_parent(parent, b)
#   if a < b:
#     parent[b] = a
#   else:
#     parent[a] = b
#
# n, m = map(int, input().split())
# parent = [0] * (n + 1)
# for i in range(1, n + 1):
#   parent[i] = i
# edges = []
# for _ in range(m):
#   a, b, cost = map(int, input().split())
#   edges.append((cost, a, b))
#
# edges.sort()
#
# result = 0
# for edge in edges:
#   cost, a, b = edge
#   if find_parent(parent, a) != find_parent(parent, b):
#     union_parent(parent, a, b)
#     result += cost
#
# print(result)
##############################################################################
# 6. topological-sort - O(V + E)
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# indegree = [0] * (n + 1)
# result = []
# for _ in range(m):
#   a, b = map(int, input().split())
#   graph[a].append(b)
#   indegree[b] += 1
#
# def topological_sort():
#   q = deque()
#   for i in range(1, n + 1):
#     if indegree[i] == 0:
#       q.append(i)
#   while q:
#     now = q.popleft()
#     result.append(now)
#     for i in graph[now]:
#       indegree[i] -= 1
#       if indegree[i] == 0:
#         q.append(i)
#
# topological_sort()
#
# for i in result:
#   print(i, end=' ')
##############################################################################
# 7. LCA(lowest common ancestor) + upgrade version
# BOJ p11437 LCA(lowest common ancestor) - O(NM)
# import sys
# from collections import deque
# input = sys.stdin.readline

# def lca(a, b):
#   while degree[a] != degree[b]:
#     if degree[a] > degree[b]:
#       a = parent[a]
#     else:
#       b = parent[b]
#   while a != b:
#     a = parent[a]
#     b = parent[b]
#   return a

# n = int(input())
# graph = [[] for _ in range(n + 1)]
# for _ in range(n - 1):
#   a, b = map(int, input().split())
#   graph[a].append(b)
#   graph[b].append(a)

# parent = [1] * (n + 1)
# visited = [False] * (n + 1)
# degree = [0] * (n + 1)

# q = deque()
# q.append(1)
# visited[1] = True
# while q:
#   now = q.popleft()
#   for i in graph[now]:
#     if not visited[i]:
#       q.append(i)
#       visited[i] = True
#       degree[i] = degree[now] + 1
#       parent[i] = now

# m = int(input())
# for _ in range(m):
#   a, b = map(int, input().split())
#   print(lca(a, b))

# BOJ p11438 LCA2 upgrade version - O(MlogN)
# import sys
# from collections import deque
# input = sys.stdin.readline
# LOG = 21 #2^20 == 1000000

# n = int(input())
# graph = [[] for _ in range(n + 1)]
# for _ in range(n - 1):
#   a, b = map(int, input().split())
#   graph[a].append(b)
#   graph[b].append(a)

# # parent table expansion by LOG
# parent = [[0] * LOG for _ in range(n + 1)]
# visited = [False] * (n + 1)
# degree = [0] * (n + 1)

# def bfs(root, depth):
#   q = deque()
#   q.append(root)
#   visited[root] = True
#   degree[root] = depth
#   while q:
#     now = q.popleft()
#     for i in graph[now]:
#       if not visited[i]:
#         q.append(i)
#         visited[i] = True
#         degree[i] = degree[now] + 1
#         parent[i][0] = now

# def set_parent():
#   bfs(1, 0)
#   for i in range(1, LOG):
#     for j in range(1, n + 1):
#       parent[j][i] = parent[parent[j][i - 1]][i - 1]

# def lca(a, b):
#   if degree[a] > degree[b]:
#     a, b = b, a
#   for i in range(LOG - 1, -1, -1):
#     if degree[b] - degree[a] >= (1 << i):
#       b = parent[b][i]
#   if a == b:
#     return a
#   for i in range(LOG - 1, -1, -1):
#     if parent[a][i] != parent[b][i]:
#       a = parent[a][i]
#       b = parent[b][i]
#   return parent[a][0]

# set_parent()

# m = int(input())
# for _ in range(m):
#   a, b = map(int, input().split())
#   print(lca(a, b))
##############################################################################
