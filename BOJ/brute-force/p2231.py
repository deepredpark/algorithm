# BOJ 2231 분해합
# N = 1,000,000 - Brute force
n = int(input())
result = 0
for i in range(1, n + 1):
  desolved_sum = sum(list(map(int, str(i))))
  if i + desolved_sum == n:
    result = i
    break

if result == 0:
  print(0)
else:
  print(result)
