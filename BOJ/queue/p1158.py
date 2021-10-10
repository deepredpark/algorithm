import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
people = deque(range(1, n+1))

i = 1
result = []
while people:
  if i != k:
    people.append(people.popleft())
    i += 1
  else:
    result.append(str(people.popleft()))
    i = 1

print('<' + ', '.join(result) + '>')
