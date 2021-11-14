# BOJ 1707 이분 그래프
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = int(1e9)

def check_visited_node(visited):
  if min(visited) != 0:
    return 0
  else:
    return visited.index(0)

def bfs(start, graph, visited):
  q = deque()
  q.append(start)
  visited[start] = 1
  while q:
    now = q.popleft()
    for i in graph[now]:
      if visited[now] == visited[i]:
        return False
      if visited[i] == 0:
        if visited[now] == 1:
          visited[i] = 2
        else:
          visited[i] = 1
        q.append(i)
  index = check_visited_node(visited)
  if index == 0:
    return True
  else:
    return bfs(index, graph, visited)

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  graph = [[] for _ in range(n + 1)]
  visited = [0] * (n + 1)
  visited[0] = INF
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  
  result = bfs(1, graph, visited)
  if result:
    print('YES')
  else:
    print('NO')
