# BOJ 1904 01타일
n = int(input())
if n == 1:
  print(1)
elif n == 2:
  print(2)
else:
  a = 1
  b = 2
  c = a + b
  for i in range(4, n + 1):
    a = b
    b = c
    c = (a + b) % 15746
  print(c % 15746)
