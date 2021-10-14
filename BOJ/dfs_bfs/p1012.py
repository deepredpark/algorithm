import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
  if matrix[i][j] == 0:
    return 0
  
  queue = deque()
  queue.append((i, j))
  matrix[i][j] = 0
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if matrix[nx][ny] > 0:
        queue.append((nx, ny))
        matrix[nx][ny] = 0
  return 1

t = int(sys.stdin.readline())
for _ in range(t):
  m, n, k = map(int, sys.stdin.readline().rstrip().split())
  matrix = [[0 for _ in range(m)] for _ in range(n)]
  for _ in range(k):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    matrix[x][y] = 1
  
  count = 0
  for i in range(n):
    for j in range(m):
      count += bfs(i, j)
  print(count)
