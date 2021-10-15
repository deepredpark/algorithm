import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
  x, y = map(int, sys.stdin.readline().split())
  matrix[x][y] = matrix[y][x] = 1

visited = [False for _ in range(n + 1)]
def bfs(start):
  if visited[start]:
    return 0
  queue = deque()
  queue.append(start)
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in range(n + 1):
      if not visited[i] and matrix[v][i] == 1:
        queue.append(i)
        visited[i] = True
  return 1

result = 0
for i in range(1, n + 1):
  result += bfs(i)

print(result)
