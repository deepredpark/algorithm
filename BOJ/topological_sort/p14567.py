# BOJ p14567 선수과목
import sys
from collections import deque

input = sys.stdin.readline

v, e = map(int, input().split())
indegree = [0] * (v + 1)
semester = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

q = deque()
for i in range(1, v + 1):
  if indegree[i] == 0:
    semester[i] = 1
    q.append(i)

while q:
  now = q.popleft()
  for i in graph[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      semester[i] = semester[now] + 1
      q.append(i)

for i in semester[1:]:
  print(i, end=' ')
