from collections import deque

graph = [[0, 1]]
for i in range(1, 200001):
  graph.append([0, i - 1, i + 1, i * 2])

def bfs(n, k):
  if n >= k:
    return (n - k)

  queue = deque()
  queue.append(n)
  
  while queue:
    v = queue.popleft()
    for i in graph[v][1:]:
      if i < 100010 and graph[i][0] == 0:
        if i == k:
          return (graph[v][0] + 1)
        queue.append(i)
        graph[i][0] = graph[v][0] + 1

n, k = map(int, input().split())
print(bfs(n, k))
