# BOJ p1912 연속합
n = int(input())
array = list(map(int, input().split()))
dp = [0] * n

if array[0] > 0:
  dp[0] = array[0]

for i in range(1, n):
  if array[i] < 0 and dp[i - 1] + array[i] < 0:
    dp[i] = 0
    continue
  dp[i] = dp[i - 1] + array[i]

result = max(dp)
if result == 0:
  print(max(array))
else:
  print(result)
