# BOJ 15651 N과 M (3)

def dfs(array):
  if len(array) == m:
    print(" ".join(map(str, array)))
    return

  for i in range(1, n + 1):
    array.append(i)
    dfs(array)
    array.pop()
     
n, m = map(int, input().split())
dfs([])
