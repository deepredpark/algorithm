# BOJ 15649 N과 M (1)
# reference = https://jamesu.dev/posts/2020/04/13/baekjoon-problem-solving-15649/

def dfs(array):
  if len(array) == m:
    print(" ".join(map(str, array)))
    return

  for i in range(1, n + 1):
    if i in array:
      continue
    array.append(i)
    dfs(array)
    array.pop()
     
n, m = map(int, input().split())
dfs([])
