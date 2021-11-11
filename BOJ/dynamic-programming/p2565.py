# BOJ 2565 전깃줄
import sys
input = sys.stdin.readline

def lis(array, dp):
  for i in range(1, len(array)):
    for j in range(i):
      if array[j] < array[i]:
        dp[i] = max(dp[i], dp[j] + 1)
  return dp

n = int(input())
array = [-1] * 501
for _ in range(n):
  a, b = map(int, input().split())
  array[a] = b

array = list(filter(lambda x: x > -1, array))
dp = [1] * len(array)
dp = lis(array, dp)
print(len(array) - max(dp))
