# Review
# DFS(Depth-First Search) 깊이 우선 탐색

# 1. Adjacency Matrix
INF = 999999999

graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0]
]

print(graph)

# 2. Adjacency List
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)

def conversion_list_to_matrix(graph):
  size = len(graph)
  matrix = [[0 for _ in range(size)] for _ in range(size)]
  for i in range(size):
    for node in graph[i]:
      matrix[i][node[0]] = node[1]
  
  return matrix

print(conversion_list_to_matrix(graph))

# 3. DFS

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' -> ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
  [],
  [2,3,8],
  [1,7],
  [4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * len(graph)
dfs(graph, 1, visited)
print()

# 4. BFS
# BFS(Breath-First Search) 너비 우선 탐색
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' -> ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
      

graph = [
  [],
  [2,3,8],
  [1,7],
  [4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * len(graph)
bfs(graph, 1, visited)
print()
