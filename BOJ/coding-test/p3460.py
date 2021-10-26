# 3460 이진수
def binary(n):
  if n <= 0:
    return ''
  return binary(n // 2) + str(n % 2)

t = int(input())
for _ in range(t):
  n = int(input())
  result = binary(n)
  result = result[::-1]
  for i in range(len(result)):
    if result[i] == '1':
      print(i, end=' ')
  print()
