# BOJ 2206 벽 부수고 이동하기
# reference = https://ca.ramel.be/82
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque()
  q.append((0, 0, 1))
  visited[0][0][1] = 1
  while q:
    x, y, w = q.popleft()
    if x == n - 1 and y == m - 1:
      return visited[x][y][w]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] == 1 and w == 1:
        visited[nx][ny][0] = visited[x][y][1] + 1
        q.append((nx, ny, 0))
      elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
        visited[nx][ny][w] = visited[x][y][w] + 1
        q.append((nx, ny, w))
  return -1

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
# boom possible = visited[_][_][1]
# boom impoosible = visited[_][_][0]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
print(bfs())
 
