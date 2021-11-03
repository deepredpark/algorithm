# BOJ p2579 계단 오르기
import sys
input = sys.stdin.readline

n = int(input())
array = [0]
for _ in range(n):
  array.append(int(input()))

if n == 1:
  print(array[1])
elif n == 2:
  print(array[1] + array[2])
elif n == 3:
  print(max(array[1], array[2]) + array[3])
else:
  dp = [0] * (301)
  dp[1] = array[1]
  dp[2] = array[1] + array[2]
  dp[3] = max(array[1], array[2]) + array[3]

  for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + array[i - 1], dp[i - 2]) + array[i]

  print(dp[n])
