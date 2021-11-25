# BOJ 1774 우주신과의 교감
import sys
from math import sqrt
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
position = [0] * (n + 1)
for i in range(1, n + 1):
  position[i] = tuple(map(int, input().split()))
for _ in range(m):
  a, b = map(int, input().split())
  union_parent(parent, a, b)
distance = []
for i in range(1, n + 1):
  for j in range(i + 1, n + 1):
    x1, y1 = position[i]
    x2, y2 = position[j]
    dist = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    distance.append((dist, i, j))

distance.sort()

result = 0
for i in range(len(distance)):
  dist, god1, god2 = distance[i]
  if find_parent(parent, god1) != find_parent(parent, god2):
    union_parent(parent, god1, god2)
    result += dist
print("{:.2f}" .format(result))
