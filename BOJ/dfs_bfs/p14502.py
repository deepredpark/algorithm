# BOJ 14502 연구소
import sys
import copy
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, walls):
  graphCopy = copy.deepcopy(graph)
  for wall in walls:
    x, y = wall
    graphCopy[x][y] = 1

  q = deque()
  for x in range(n):
    for y in range(m):
      if graphCopy[x][y] == 2:
        q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graphCopy[nx][ny] == 0:
        graphCopy[nx][ny] = 2
        q.append((nx, ny))
  count = 0
  for x in range(n):
    for y in range(m):
      if graphCopy[x][y] == 0:
        count += 1
  return count

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
walls = []
for x in range(n):
  for y in range(m):
    if graph[x][y] == 0:
      walls.append((x, y))

result = 0
for i in range(len(walls)):
  for j in range(i + 1, len(walls)):
    for k in range(j + 1, len(walls)):
      safeCount = bfs(graph, [walls[i], walls[j], walls[k]])
      result = max(result, safeCount)
print(result)
