# BOJ p2133 타일채우기
# reference = https://codedrive.tistory.com/188

n = int(input())
dp = [0] * 31

# 계산용
dp[0] = 1
addition = 0
for i in range(2, n + 1, 2):
  dp[i] = dp[i - 2] * 3 + addition * 2
  addition += dp[i - 2]

print(dp[n])
