import sys
from collections import deque

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in sorted(graph[v]):
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, v, visited):
  queue = deque()
  visited[v] = True
  queue.append(v)
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in sorted(graph[v]):
      if not visited[i]:
        visited[i] = True
        queue.append(i)

n, m, start = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  node1, node2 = map(int, sys.stdin.readline().rstrip().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

visited = [False] * (n + 1)
dfs(graph, start, visited)
print()
visited = [False] * (n + 1)
bfs(graph, start, visited)
