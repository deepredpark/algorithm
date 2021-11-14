# BOJ 1874 스택 수열
import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]

index = 0
result = []
result_calc = []
for i in range(1, n + 1):
  result.append(i)
  result_calc.append('+')
  if i == array[index]:
    result.pop()
    result_calc.append('-')
    index += 1
    for j in range(i - 1, 0, -1):
      if result == []:
        break
      if array[index] == result[-1]:
        result.pop()
        result_calc.append('-')
        index += 1
      else:
        break

if result == []:
  for i in result_calc:
    print(i)
else:
  print('NO')
