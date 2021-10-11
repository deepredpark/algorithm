import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
  n, pointer = map(int, sys.stdin.readline().split())
  documents = deque(map(int, sys.stdin.readline().split()))
  count = 0

  while True:
    max_document = max(documents)
    if documents[0] == max_document:
      count += 1
      if pointer == 0:
        print(count)
        break
      else:
        documents.popleft()
        pointer -= 1
    else:
      documents.append(documents.popleft())
      if pointer == 0:
        pointer = len(documents)-1
      else:
        pointer -= 1
