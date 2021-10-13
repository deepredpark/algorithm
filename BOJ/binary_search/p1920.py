import sys

n = int(sys.stdin.readline())
array_n = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
array_m = list(map(int, sys.stdin.readline().rstrip().split()))

array_n.sort()
def binary_search(array, start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] < target:
      start = mid + 1
    elif array[mid] > target:
      end = mid - 1
    else:
      return 1
  return 0

for i in array_m:
  print(binary_search(array_n, 0, n - 1, i))
