# BOJ 4386 별자리 만들기
import sys
import math
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

n = int(input())
parent = [0] * (n + 1)
for i in range(1, n + 1):
  parent[i] = i
position = [0] * (n + 1)
for i in range(1, n + 1):
  x, y = map(float, input().split())
  position[i] = (x, y)
distance = []
for i in range(1, n + 1):
  for j in range(i + 1, n + 1):
    x1, y1 = position[i]
    x2, y2 = position[j]
    dist = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    dist = round(dist, 2)
    distance.append((dist, i, j))

distance.sort()

result = 0
for i in range(len(distance)):
  dist, star1, star2 = distance[i]
  if find_parent(parent, star1) != find_parent(parent, star2):
    union_parent(parent, star1, star2)
    result += dist
print(result)
