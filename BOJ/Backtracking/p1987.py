# BOJ 1987 알파벳
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(point, path, count):
  global result
  result = max(result, count)
  
  x, y = point
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    if visited[graph[nx][ny]] == 0:
      visited[graph[nx][ny]] = 1
      dfs((nx, ny), visited, count + 1)
      visited[graph[nx][ny]] = 0

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(lambda x: ord(x) - ord('A'), input().rstrip())))
visited = [0] * 26
result = 0
visited[graph[0][0]] = 1
dfs((0,0), visited, 1)
print(result)
