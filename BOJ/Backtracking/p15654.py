# BOJ 15654 N과 M (5)

def permutations(result):
  if len(result) == m:
    print(" ".join(map(str, result)))
    return
  for i in range(n):
    if array[i] in result:
      continue
    result.append(array[i])
    permutations(result)
    result.pop()

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
permutations([])
