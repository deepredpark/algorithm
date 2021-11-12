# BOJ 2798 블랙잭
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
max_result = array[1] + array[2] + array[3]
for i in range(n - 2):
  if array[i] >= m or max_result == m:
    break
  for j in range(i + 1, n - 1):
    if array[j] >= m:
      break
    for k in range(j + 1, n):
      if array[k] >= m:
        break
      result = array[i] + array[j] + array[k]
      if result <= m and result > max_result:
        max_result = result
      elif result == m:
        max_result = result
        break

print(max_result)
