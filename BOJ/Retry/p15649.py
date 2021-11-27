# Retry - Backtracking
# BOJ 15649 N과 M(1)
def permutations(result):
  if len(result) == m:
    print(" ".join(map(str, result)))
    return
  for i in range(1, n + 1):
    if i in result:
      continue
    result.append(i)
    permutations(result)
    result.pop()

n, m = map(int, input().split())
permutations([])
