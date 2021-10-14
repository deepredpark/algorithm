import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  queue = deque()
  
  for i in range(n):
    for j in range(m):
      if matrix[i][j] == 1:
        queue.append((i, j))
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if matrix[nx][ny] == 0:
        queue.append((nx, ny))
        matrix[nx][ny] = matrix[x][y] + 1
        
  
m, n = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
  matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

bfs()

max_day = 1
for i in range(n):
  max_day = max(max_day, max(matrix[i]))
  for j in range(m):
    if matrix[i][j] == 0:
      max_day = 0
      break
  if max_day == 0:
    break
    
print(max_day - 1)
