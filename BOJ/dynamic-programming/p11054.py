# BOJ 11054 가장 긴 바이토닉 부분 수열
def lis(array, dp):
  for i in range(1, len(array)):
    for j in range(i):
      if array[j] < array[i]:
        dp[i] = max(dp[i], dp[j] + 1)
  return dp

n = int(input())
array = list(map(int, input().split()))
lis_dp = [1] * n
lis_dp = lis(array, lis_dp)
lls_dp = [1] * n
lls_dp = lis(array[::-1], lls_dp)
lls_dp.reverse()
sum_dp = [0] * n
for i in range(n):
  sum_dp[i] = lis_dp[i] + lls_dp[i]
print(max(sum_dp) - 1)
