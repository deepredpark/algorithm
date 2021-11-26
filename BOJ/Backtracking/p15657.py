# BOJ 15657 N과 M (8)

def dfs(start, result):
  if len(result) == m:
    print(" ".join(map(str, result)))
    return
  for i in range(start, n):
    result.append(array[i])
    dfs(i, result)
    result.pop()

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
dfs(0, [])
