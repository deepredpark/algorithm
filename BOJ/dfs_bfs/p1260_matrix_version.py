# Adjacency Matrix version
import sys
from collections import deque

def dfs(n, matrix, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in range(n + 1):
    if not visited[i] and matrix[v][i] == 1:
      dfs(n, matrix, i, visited)

def bfs(n, matrix, v, visited):
  queue = deque()
  visited[v] = True
  queue.append(v)
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in range(n + 1):
      if not visited[i] and matrix[v][i] == 1:
        visited[i] = True
        queue.append(i)

n, m, start = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
  node1, node2 = map(int, sys.stdin.readline().rstrip().split())
  matrix[node1][node2] = matrix[node2][node1] = 1
  
visited = [False] * (n + 1)
dfs(n, matrix, start, visited)
print()
visited = [False] * (n + 1)
bfs(n, matrix, start, visited)
