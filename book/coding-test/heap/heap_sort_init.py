# python min-heap

import sys
import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

n = int(input())
arr = []

for i in range(n):
  arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
  print(res[i])
