# DFS review page149
# import sys
# from collections import deque

# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#   graph.append(list(map(int, input().rstrip())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x, y):
#   if graph[x][y] == 1:
#     return 0
#   q = deque()
#   q.append((x, y))
#   graph[x][y] = 1
#   while q:
#     nx, ny = q.popleft()
#     for i in range(4):
#       x = nx + dx[i]
#       y = ny + dy[i]
#       if x < 0 or y < 0 or x >= n or y >= m:
#         continue
#       if graph[x][y] == 0:
#         q.append((x, y))
#         graph[x][y] = 1
#   return 1

# result = 0
# for x in range(n):
#   for y in range(m):
#     result += bfs(x, y)

# print(result)
# BFS review page152
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))
visited[0][0] = True
while q:
  nx, ny = q.popleft()
  for i in range(4):
    x = nx + dx[i]
    y = ny + dy[i]
    if x < 0 or y < 0 or x >= n or y >= m:
      continue
    if not visited[x][y] and graph[x][y] != 0:
      graph[x][y] += graph[nx][ny]
      q.append((x, y))
      visited[x][y] = True

for x in range(n):
  for y in range(m):
    print('{0:2}' .format(graph[x][y]), end=' ')
  print()
