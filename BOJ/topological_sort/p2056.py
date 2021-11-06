# BOJ p2056 작업
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)
dp = [0] * (n + 1)
for i in range(1, n + 1):
  work_info = list(map(int, input().split()))
  time[i] = work_info[0]
  mini_n = work_info[1]
  for j in work_info[2:]:
    graph[j].append(i)
    indegree[i] += 1

q = deque()
for i in range(1, n + 1):
  if indegree[i] == 0:
    dp[i] = time[i]
    q.append(i)
while q:
  now = q.popleft()
  for i in graph[now]:
    indegree[i] -= 1
    dp[i] = max(dp[i], dp[now] + time[i])
    if indegree[i] == 0:
      q.append(i)

print(max(dp[1:]))
