# BOJ 15650 N과 M (2)

def dfs(start, array):
  if len(array) == m:
    print(" ".join(map(str, array)))
    return

  for i in range(start, n + 1):
    if i in array:
      continue
    array.append(i)
    dfs(i + 1, array)
    array.pop()
     
n, m = map(int, input().split())
dfs(1, [])
