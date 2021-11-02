# shortest path PS
# page259 미래도시 14 min
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
  for y in range(1, n + 1):
    if x == y:
      graph[x][y] = 0

for _ in range(m):
  x, y = map(int, input().split())
  graph[x][y] = graph[y][x] = 1

target, mid_target = map(int, input().split())

for k in range(1, n + 1):
  for x in range(1, n + 1):
    for y in range(1, n + 1):
      graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

result = graph[1][mid_target] + graph[mid_target][target]

if result >= INF:
  print(-1)
else:
  print(result)

# page262 전보 20 min
# 개선된 다익스트라 사용하고, 결과는 출발노드 제외 INF 없는 도시 갯수, 최소시간들의 최댓값 2개 출력
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_value = 0
for i in range(1, n + 1):
  if distance[i] != INF:
    count += 1
    max_value = max(max_value, distance[i])

print(count - 1, max_value)
