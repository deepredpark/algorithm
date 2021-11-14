# BOJ 9012 괄호(Parenthesis String, PS)
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  PS = input().rstrip()
  result = 0
  for i in PS:
    if i == '(':
      result += 1
    else:
      result -= 1
      if result < 0:
        break
  if result == 0:
    print('YES')
  else:
    print('NO')
