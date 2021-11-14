# BOJ 10773 제로
import sys
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
  k = int(input())
  if k == 0:
    result.pop()
    continue
  result.append(k)
print(sum(result))
