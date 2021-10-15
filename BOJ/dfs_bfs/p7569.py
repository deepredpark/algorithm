import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(h)]
for i in range(h):
  for _ in range(n):
    graph[i].append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
  queue = deque()

  for i in range(h):
    for j in range(n):
      for k in range(m):
        if graph[i][j][k] == 1:
          queue.append((j, k, i))
  
  while queue:
    x, y, z = queue.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
        continue
      if graph[nz][nx][ny] == 0:
        queue.append((nx, ny, nz))
        graph[nz][nx][ny] = graph[z][x][y] + 1

bfs()

max_day = 1
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 0:
        print(-1)
        exit(0)
      else:
        max_day = max(max_day, graph[i][j][k])

print(max_day - 1)
