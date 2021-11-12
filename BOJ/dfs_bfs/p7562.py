# BOJ 7562 나이트의 이동
# BFS
import sys
from collections import deque

input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(graph, visited, start, target):
  q = deque()
  a, b = start
  visited[a][b] = True
  q.append(start)
  while q:
    x, y = q.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if not visited[nx][ny]:
        graph[nx][ny] = graph[x][y] + 1
        visited[nx][ny] = True
        q.append((nx, ny))

  a, b = target
  return graph[a][b]

t = int(input())
for _ in range(t):
  n = int(input())
  graph = [[0] * n for _ in range(n)]
  visited = [[False] * n for _ in range(n)]
  start = tuple(map(int, input().split()))
  target = tuple(map(int, input().split()))
  
  print(bfs(graph, visited, start, target))
