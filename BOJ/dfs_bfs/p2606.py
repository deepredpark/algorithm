import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  matrix[x][y] = matrix[y][x] = 1

visited = [False for _ in range(n + 1)]

start = 1
queue = deque()
queue.append(start)
visited[start] = True

count = 0
while queue:
  v = queue.popleft()
  for i in range(1, n + 1):
    if (matrix[v][i] == 1) and (not visited[i]):
      queue.append(i)
      visited[i] = True
      count += 1

print(count)
