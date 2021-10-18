# page 380 - 33 min
# My solution

n = int(input())
array = list(map(int, input().split()))
count = [0] * n

start = array[0]
count[0] = 1
for i in range(1, n):
  count_case = []
  for j in range(i - 1, -1, -1):
    if array[i] <= array[j]:
      count_case.append(count[j])
    
    if count_case:
      count[i] = max(count_case) + 1
    else:
      count[i] = 1

print(count)
print(n - max(count))

# solution - Dongbin Na
# 가장 긴 증가하는 부분 수열 LIS(Longest Increasing Subsequence) algorithm

n = int(input())
array = list(map(int, input().split()))

# 순서를 뒤집어 'LIS' 문제로 변환
array.reverse()

dp = [1] * n

for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
