# BOJ 14889 스타트와 링크
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

array = [x for x in range(n)]
teams = list(combinations(array, n // 2))
result = int(1e9)
for i in range(len(teams) // 2):
  team1 = teams[i]
  team2 = teams[-i-1]
  sum1 = 0; sum2 = 0
  for i, j in combinations(list(range(n // 2)), 2):
    a, b = team1[i], team1[j]
    sum1 += graph[a][b]
    sum1 += graph[b][a]
    a, b = team2[i], team2[j]
    sum2 += graph[a][b]
    sum2 += graph[b][a]
  result = min(result, abs(sum1 - sum2))
print(result)
