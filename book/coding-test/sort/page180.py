# 두 배열의 원소 교체 page182
# My solution

from collections import deque

n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a = deque(sorted(array_a))
array_b = deque(sorted(array_b))

for i in range(k):
  if array_b[-1] > array_a[0]:
    array_b.appendleft(array_a.popleft())
    array_a.append(array_b.pop())
    print(array_a)
  else:
    break

sum = 0
for i in array_a:
  sum += i

print(sum)

# Dongbin Na
# 핵심 아이디어: 매번 배열 A에서 가장 작은 원소를 골라서 배열 B에서 가장 큰 원소와 교체

n, k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)

for i in range(k):
  if array_a[i] < array_b[i]:
    array_a[i], array_b[i] = array_b[i], array_a[i]
  else:
    break

print(sum(a))
