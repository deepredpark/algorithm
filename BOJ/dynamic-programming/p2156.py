# BOJ p2156 포도주 시식
import sys
input = sys.stdin.readline

n = int(input())
array = [0]
for _ in range(n):
  array.append(int(input()))

dp = [0] * (n + 1)
if n == 1:
  print(array[1])
elif n == 2:
  print(array[1] + array[2])
elif n == 3:
  print(array[1] + array[2] + array[3] - min(array[1:]))
else:
  dp[1] = array[1]
  dp[2] = array[1] + array[2]
  dp[3] = array[1] + array[2] + array[3] - min(array[1:4])
  for i in range(4, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i], dp[i - 3] + array[i] + array[i - 1])
  print(dp[n])
