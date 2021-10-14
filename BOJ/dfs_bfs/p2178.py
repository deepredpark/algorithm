import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
  matrix.append(list(map(int, sys.stdin.readline().rstrip())))
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0))
visited[0][0] = True
while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    if (not visited[nx][ny]) and (matrix[nx][ny] > 0):
      queue.append((nx, ny))
      visited[nx][ny] = True
      matrix[nx][ny] += matrix[x][y]

print(matrix[n - 1][m - 1])
