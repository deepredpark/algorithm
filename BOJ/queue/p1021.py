# BOJ 1021 회전하는 큐
from collections import deque

n, m = map(int, input().split())
array = deque([x for x in range(1, n + 1)])
result = list(map(int, input().split()))
count = 0
for i in result:
  if array.index(i) <= len(array) - array.index(i):
    while array[0] != i:
      array.append(array.popleft())
      count += 1
    else:
      array.popleft()
  else:
    while array[0] != i:
      array.appendleft(array.pop())
      count += 1
    else:
      array.popleft()
print(count)
