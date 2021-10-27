# BOJ p14002 가장 긴 증가 부분 수열 4
n = int(input())
array = list(map(int, input().split()))

dp = [1] * n
dp2 = [[x] for x in array]

for i in range(1, n):
  max_index = i
  for j in range(i):
    if array[j] < array[i] and dp[j] >= dp[max_index]:
      max_index = j
  if max_index != i:
    dp[i] = dp[max_index] + 1
    dp2[i].extend(dp2[max_index])

index = 0
for i in range(1, n):
  if dp[index] < dp[i]:
    index = i

print(dp[index])
for k in sorted(dp2[index]):
  print(k, end=' ')
