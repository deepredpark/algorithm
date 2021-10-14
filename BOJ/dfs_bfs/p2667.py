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

  result = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if matrix[nx][ny] > 0:
        queue.append((nx, ny))
        matrix[nx][ny] = 0
        result += 1
  return result

n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
  matrix.append(list(map(int, sys.stdin.readline().rstrip())))

count_complex = 0
count_house = []
for i in range(n):
  for j in range(n):
    count = bfs(i, j)
    if count > 0:
      count_house.append(count)
      count_complex += 1

print(count_complex)
count_house.sort()
for i in count_house:
  print(i)
