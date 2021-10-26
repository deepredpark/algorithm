# p2501 약수 구하기
n, k = map(int, input().split())

count = 0
result = 0
for i in range(1, n + 1):
  if n % i == 0:
    count += 1
    result = i
    if count == k:
      break

if count != k:
  print(0)
else:
  print(result)
