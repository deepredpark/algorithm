# BOJ 5430 AC
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  p = input().rstrip()
  n = int(input())
  array = input().rstrip()
  q = deque(array[1:-1].split(','))
  if n == 0:
    q = deque([])

  reverse = False
  error = False
  for i in p:
    if i == 'R':
      if reverse:
        reverse = False
      else:
        reverse = True
    else:
      if len(q) == 0:
        error = True
        break
      else:
        if reverse:
          q.pop()
        else:
          q.popleft()
  
  if error:
    print('error')
  else:
    if reverse:
      q = reversed(q)
    print('[' + ','.join(q) + ']')
