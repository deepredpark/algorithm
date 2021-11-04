# BOJ p1932 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
tree = [0]
for _ in range(n):
  tree.extend(list(map(int, input().split())))
dp = [0] * len(tree)
if n == 1:
  print(tree[1])
elif n == 2:
  print(tree[1] + max(tree[2], tree[3]))
else:
  dp[1] = tree[1]
  dp[2] = dp[1] + tree[2]
  dp[3] = dp[1] + tree[3]

  # 2층까지의 노드 갯수
  total = 3
  # 2층 노드 갯수
  floor_total = 2 
  for i in range(4, len(tree)):
    if i == total + 1:
      dp[i] = dp[i - floor_total] + tree[i]
    elif i == total + (floor_total + 1):
      dp[i] = dp[i - floor_total - 1] + tree[i]
      floor_total += 1
      total += floor_total
    else:
      dp[i] = max(dp[i - floor_total - 1], dp[i - floor_total]) + tree[i]

  print(max(dp[-n:]))
