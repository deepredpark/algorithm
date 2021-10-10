import sys

n = int(sys.stdin.readline())

for i in range(n):
  words = sys.stdin.readline().split()
  print('Case #{0}:' .format(i+1), end=' ')
  while words:
    print(words.pop(), end=' ')
  print()
