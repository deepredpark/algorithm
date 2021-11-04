# BOJ p9465 스티커
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  
  n = int(input())
  array = [[0], [0], [0]]
  for i in range(1, 3):
    array[i] += list(map(int, input().split()))
  
  dp = [0] * (n + 1)
  
  if n == 1:
    print(max(array[1][1], array[2][1]))
    continue
  
  dp[1] = max(array[1][1], array[2][1])
  array[1][2] = array[2][1] + array[1][2]
  array[2][2] = array[1][1] + array[2][2]
  dp[2] = max(array[1][2], array[2][2])
  
  for j in range(3, n + 1):
    array[1][j] = max(array[2][j - 1], dp[j - 2]) + array[1][j]
    array[2][j] = max(array[1][j - 1], dp[j - 2]) + array[2][j]
    dp[j] = max(array[1][j], array[2][j])
  
  print(dp[n])
