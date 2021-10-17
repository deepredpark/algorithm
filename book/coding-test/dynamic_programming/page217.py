# page 217 - 27 min
# My solution

from collections import deque

n = 30000
count = [0] * (n + 1)
queue = deque()
queue.append(n)
while queue:
  v = queue.popleft()
  node = []
  if v == 1:
    break
  
  if v % 5 == 0:
    node.append(v // 5)
  if v % 3 == 0:
    node.append(v // 3)
  if v % 2 == 0:
    node.append(v // 2)
  node.append(v - 1)

  for i in node:
    if i > 0 and count[i] == 0:
      queue.append(i)
      count[i] = count[v] + 1

print(count[1])
