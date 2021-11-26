# BOJ 1182 부분수열의 합
# reference = https://seongonion.tistory.com/98 (backtracking idea)
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))
count = 0

def dfs(i, sum):
  global count
  if i >= n:
    return
  sum += array[i]
  if sum == s:
    count += 1

  dfs(i + 1, sum)
  dfs(i + 1, sum - array[i])

dfs(0, 0)
print(count)
