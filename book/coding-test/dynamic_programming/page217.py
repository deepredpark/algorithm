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

# solution - Dongbin Na
# a[i] = min(a[i-1], a[i/2], a[i/3], a[i/5]) + 1

x = int(input())
d = [0] * 30001

for i in range(2, x + 1):
  d[i] = d[i - 1] + 1
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)
  
print(d[x])



