import sys

def binary_search(array, start, end, target):
  result = 0
  while start <= end:
    mid = (start + end) // 2
    if array[mid] < target:
      start = mid + 1
    elif array[mid] > target:
      end = mid - 1
    else:
      result = 1
      break
  return result

T = int(sys.stdin.readline())

for _ in range(T):
  a = int(sys.stdin.readline())
  array_a = list(map(int, sys.stdin.readline().rstrip().split()))
  b = int(sys.stdin.readline())
  array_b = list(map(int, sys.stdin.readline().rstrip().split()))
  array_a.sort()

  for i in array_b:
    print(binary_search(array_a, 0, a - 1, i))
