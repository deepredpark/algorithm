# BOJ p11437 LCA
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [False] * (n + 1)
degree = [0] * (n + 1)

def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = True
  while q:
    now = q.popleft()
    for i in graph[now]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        parent[i] = now
        degree[i] = degree[now] + 1

def LCA(a, b):
  while degree[a] != degree[b]:
    if degree[a] < degree[b]:
      b = parent[b]
    else:
      a = parent[a]
  while a != b:
    a = parent[a]
    b = parent[b]
  return a

bfs(1)

m = int(input())
for _ in range(m):
  a, b = map(int, input().split())
  print(LCA(a, b))
