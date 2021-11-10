# BOJ p11438 LCA2 upgrade version 
import sys
from collections import deque
input = sys.stdin.readline
LOG = 21 #2^20 == 1000000

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# parent table expansion by LOG
parent = [[0] * LOG for _ in range(n + 1)]
visited = [False] * (n + 1)
degree = [0] * (n + 1)

def bfs(root, depth):
  q = deque()
  q.append(root)
  visited[root] = True
  degree[root] = depth
  while q:
    now = q.popleft()
    for i in graph[now]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        degree[i] = degree[now] + 1
        parent[i][0] = now

def set_parent():
  bfs(1, 0)
  for i in range(1, LOG):
    for j in range(1, n + 1):
      parent[j][i] = parent[parent[j][i - 1]][i - 1]

def lca(a, b):
  if degree[a] > degree[b]:
    a, b = b, a
  for i in range(LOG - 1, -1, -1):
    if degree[b] - degree[a] >= (1 << i):
      b = parent[b][i]
  if a == b:
    return a
  for i in range(LOG - 1, -1, -1):
    if parent[a][i] != parent[b][i]:
      a = parent[a][i]
      b = parent[b][i]
  return parent[a][0]

set_parent()

m = int(input())
for _ in range(m):
  a, b = map(int, input().split())
  print(lca(a, b))
