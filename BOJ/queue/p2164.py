# BOJ 2164 카드2
from collections import deque

n = int(input())
q = deque([x for x in range(1, n + 1)])
for _ in range(n - 1):
  q.popleft()
  q.append(q.popleft())

print(q[0])
