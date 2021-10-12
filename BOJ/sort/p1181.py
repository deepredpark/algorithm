import sys

n = int(sys.stdin.readline())
words = []
for _ in range(n):
  words.append(sys.stdin.readline().rstrip())

words = sorted(set(words))
words.sort(key=lambda x: len(x))

for i in words:
  print(i)
