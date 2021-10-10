import sys

def binary(n):
  if n // 2 == 0:
    print(n, end='')
    return
  binary(n // 2)
  print(n % 2, end='')

n = int(sys.stdin.readline())
binary(n)
