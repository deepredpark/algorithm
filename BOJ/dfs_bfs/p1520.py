# BOJ 1520 내리막 길
import sys
import heapq
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(graph):
  q = []
  heapq.heappush(q, (-graph[0][0], 0, 0))
  visited[0][0] = 1
  while q:
    height, x, y = heapq.heappop(q)
    height *= -1
    if x == n - 1 and y == m - 1:
      continue
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] < height:
        if visited[nx][ny] == 0:
          heapq.heappush(q, (-graph[nx][ny], nx, ny))
        visited[nx][ny] += visited[x][y]

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]
bfs(graph)
print(visited[n - 1][m - 1])
