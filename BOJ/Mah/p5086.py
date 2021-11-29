# BOJ 5086 배수와 약수
import sys
input = sys.stdin.readline

while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break
  if n > m:
    if n % m == 0:
      print('multiple')
      continue
  else:
    if m % n == 0:
      print('factor')
      continue
  print('neither')
