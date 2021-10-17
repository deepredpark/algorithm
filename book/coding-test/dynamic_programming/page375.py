# page 375 - 33 min
# My solution

import sys

t = int(sys.stdin.readline())
for _ in range(t):
  n, m = map(int, sys.stdin.readline().split())
  line = list(map(int, sys.stdin.readline().rstrip().split()))
  array = []
  for i in range(n):
    array.append(line[4 * i:4 * (i + 1)])

  result = 0
  for j in range(m - 1):
    for i in range(n):
      if i == 0:
        array[i][j + 1] = max(array[i][j], array[i + 1][j]) + array[i][j + 1]
      elif i == n - 1:
        array[i][j + 1] = max(array[i][j], array[i - 1][j]) + array[i][j + 1]
      else:
        array[i][j + 1] = max(array[i][j], array[i - 1][j], array[i + 1][0]) + array[i][j + 1]
      result = max(result, array[i][j + 1])
    
  print(result)

# solution - Dongbin Na
# dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

for _ in range(int(sys.stdin.readline())):
  n, m = map(int, sys.stdin.readline().split())
  array = list(map(int, sys.stdin.readline().rstrip().split()))
  dp = []
  index = 0
  for i in range(n):
    dp.append(array[index:index + m])
    index += m
  
  for j in range(1, m):
    for i in range(n):
      if i == 0: left_up = 0
      else: left_up = dp[i - 1][j - 1]
      if i == n - 1: left_down = 0
      else: left_down = dp[i + 1][j - 1]
      left = dp[i][j - 1]
      dp[i][j] = dp[i][j] + max(left_up, left, left_down)
  
  result = 0
  for i in range(n):
    result = max(result, dp[i][m - 1])
  print(result)
