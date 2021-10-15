from collections import deque

Max = 100000
graph = [0] * (Max + 1)

def bfs(n, k):
  if n >= k:
    return (n - k)

  queue = deque()
  queue.append(n)
  
  while queue:
    v = queue.popleft()
    for i in (v - 1, v + 1, v * 2):
      if 0 <= i <= Max and graph[i] == 0:
        if i == k:
          return (graph[v] + 1)
        queue.append(i)
        graph[i] = graph[v] + 1

n, k = map(int, input().split())
print(bfs(n, k))
