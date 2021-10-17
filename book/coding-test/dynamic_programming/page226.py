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

# solution - Dongbin Na
# a[i - k]를 만드는 방법이 존재하는 경우, a[i] = min(a[i], a[i - k] + 1)
# a[i - k]를 만드는 방법이 존재하지 않는 경우, a[i] = 10,001

n, m = map(int, sys.stdin.readline().split())
array = []
for _ in range(n):
  array.append(int(sys.stdin.readline()))
d = [10001] * (m + 1)
d[0]
for i in range(n):
  for j in range(array[i], m +1):
    if d[j - array[i]] != 10001:
      d[j] = min(d[j], d[j - array[i]] + 1)
      
if d[m] == 10001:
  print(-1)
else:
  print(d[m])
    
