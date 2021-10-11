from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if (graph[nx][ny] == 1) and (not visited[nx][ny]):
        graph[nx][ny] = graph[x][y] + 1
        visited[nx][ny] = True
        queue.append((nx, ny))
    
  return graph[n - 1][m - 1]

print(bfs(0, 0, visited))
