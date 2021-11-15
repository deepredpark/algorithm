# BOJ 11866 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())
q = deque([str(x) for x in range(1, n + 1)])
result = []
for i in range(n):
  for j in range(k - 1):
    q.append(q.popleft())
  result.append(q.popleft())

print('<' + ', '.join(result) + '>')
