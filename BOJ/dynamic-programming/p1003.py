# BOJ p1003 피보나치 함수
import sys
input = sys.stdin.readline

t = int(input())
n = []
for _ in range(t):
  n.append(int(input()))

max_n = max(n)
dp = [[0, 0] for _ in range(max_n + 1)]
# dp[1] = [0, 1] = 재귀함수 fibo(1)이 호출될 때, fibo(0) : fibo(1) 호출 수 = 0 : 1
dp[0] = [1, 0]
dp[1] = [0, 1]
for i in range(2, max_n + 1):
  dp[i] = [dp[i-1][0] + dp[i - 2][0], dp[i-1][1] + dp[i - 2][1]]

for i in n:
  print(dp[i][0], dp[i][1])
