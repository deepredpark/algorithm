import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().rstrip().split()))

a = list(map(lambda x: x + 10000000, a))
b = list(map(lambda x: x + 10000000, b))

count_list = [0] * 20000001

for i in range(n):
  count_list[a[i]] += 1

for i in range(m):
  if count_list[b[i]] > 0:
    print(1, end=' ')
  else:
    print(0, end=' ')
