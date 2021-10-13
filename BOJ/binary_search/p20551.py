import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a = []
q = []
for _ in range(n):
  a.append(int(sys.stdin.readline()))
for _ in range(m):
  q.append(int(sys.stdin.readline()))

a. sort()

def binary_search(array, start, end, target):
  result = -1
  while start <= end:
    mid = (start + end) // 2
    if array[mid] < target:
      start = mid + 1
    elif array[mid] > target:
      end = mid - 1
    else:
      result = mid
      end = mid - 1
  return result

for i in q:
  print(binary_search(a, 0, n - 1, i))
