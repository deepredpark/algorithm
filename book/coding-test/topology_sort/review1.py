# First, Topological sort review
import sys
from collections import deque

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
indegree = [0] * (v + 1)
result = []

for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

def topological_sort():
  q = deque()
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
  
  for i in result:
    print(i, end=' ')

topological_sort()
