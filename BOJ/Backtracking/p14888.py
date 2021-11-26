# BOJ 14888 연산자 끼워넣기
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
calc = list(map(int, input().split()))

max_value = -int(1e9)
min_value = int(1e9)
def dfs(i, sum, plus, minus, mul, div):
  global max_value
  global min_value
  if plus < 0 or minus < 0 or mul < 0 or div < 0:
    return
  if i == n - 1:
    max_value = max(max_value, sum)
    min_value = min(min_value, sum)
    return
  dfs(i + 1, sum + array[i + 1], plus - 1, minus, mul, div)
  dfs(i + 1, sum - array[i + 1], plus, minus - 1, mul, div)
  dfs(i + 1, sum * array[i + 1], plus, minus, mul - 1, div)
  dfs(i + 1, -(-sum // array[i + 1]) if sum * array[i + 1] < 0 else sum // array[i + 1] , plus, minus, mul, div - 1)

dfs(0, array[0], calc[0], calc[1], calc[2], calc[3])
print(max_value)
print(min_value)
