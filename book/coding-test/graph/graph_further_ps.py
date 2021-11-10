# 팀결성 page 298
import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(n + 1):
  parent[i] = i

for _ in range(m):
  command, a, b = map(int, input().split())
  if command == 0:
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
  else:
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a == root_b:
      print('YES')
    else:
      print('NO')
      
# 도시분할계획 page300
import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n + 1):
  parent[i] = i

edges = []
for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()

result = []
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result.append(cost)

result.pop()
print(sum(result))

# 커리큘럼 page303
import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
cost = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for i in range(1, n + 1):
  line = list(map(int, input().split()))
  line.pop()
  cost[i] = line[0]
  if len(line) > 1:
    indegree[i] += len(line[1:])
    for j in line[1:]:
      graph[j].append(i)

dp_cost = cost[:]
q = deque()
for i in range(1, n + 1):
  if indegree[i] == 0:
    q.append(i)
while q:
  now = q.popleft()
  for i in graph[now]:
    indegree[i] -= 1
    dp_cost[i] = max(dp_cost[i], dp_cost[now] + cost[i])
    if indegree[i] == 0:
      q.append(i)

for i in range(1, n + 1):
  print(dp_cost[i])
