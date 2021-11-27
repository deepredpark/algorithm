# Retry - Backtracking
# BOJ 14888 연산자 끼워넣기
def dfs(i, sum, plus, minus, mul, div):
  global maxValue
  global minValue
  if plus < 0 or minus < 0 or mul < 0 or div < 0:
    return
  if i == n - 1:
    maxValue = max(maxValue, sum)
    minValue = min(minValue, sum)
    return
  dfs(i + 1, sum + array[i + 1], plus - 1, minus, mul, div)
  dfs(i + 1, sum - array[i + 1], plus, minus - 1, mul, div)
  dfs(i + 1, sum * array[i + 1], plus, minus, mul - 1, div)
  dfs(i + 1, -(-sum // array[i + 1]) if sum * array[i + 1] < 0 else sum // array[i + 1], plus, minus, mul, div - 1)

n = int(input())
array = list(map(int, input().split()))
oper = list(map(int, input().split()))
maxValue = -int(1e9)
minValue = int(1e9)
dfs(0, array[0], oper[0], oper[1], oper[2], oper[3])
print(maxValue)
print(minValue)
