import sys
from collections import deque

n = int(sys.stdin.readline())
cards = deque(range(1, n+1))
for _ in range(n-1):
  print(cards.popleft(), end=' ')
  cards.append(cards.popleft())

print(cards[0])
