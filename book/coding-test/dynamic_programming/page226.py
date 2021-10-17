# page 226 27 min
# My solution

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
  coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)
count = [0] * (m + 1)

queue = deque()
queue.append(0)

while queue:
  x = queue.popleft()
  if x == m:
    break
  for i in range(len(coins)):
    nx = x + coins[i]
    if nx > m:
      continue
    if count[nx] == 0:
      queue.append(nx)
      count[nx] = count[x] + 1

if count[m] == 0:
  print(-1)
else: 
  print(count[m])
