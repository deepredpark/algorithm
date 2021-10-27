# page223 바닥공사

# My solution - Incorrect

n = int(input())

start1 = 3 ** (n // 2)
start2 = 3 ** ((n - 1) // 2)

print((start1 + start2 - 1) % 796796)

# solution

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
  dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[n] % 796796)
