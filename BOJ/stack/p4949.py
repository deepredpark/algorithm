# BOJ 4949 균형잡힌 세상
import sys
input = sys.stdin.readline

while True:
  line = input().rstrip()
  if line == '.':
    break

  result = []
  for i in line:
    if i == '[' or i == '(':
      result.append(i)
      continue
    if i == ']':
      if result == [] or result[-1] != '[':
        result = [-1]
        break
      else:
        result.pop()  
    elif i == ')':
      if result == [] or result[-1] != '(':
        result = [-1]
        break
      else:
        result.pop()

  if not result:
    print('yes')
  else:
    print('no')
