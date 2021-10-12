import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
  name, x = sys.stdin.readline().split()
  array.append((name, int(x)))

array.sort(key=lambda x: x[1])
for i in array:
  print(i[0], end=' ')
