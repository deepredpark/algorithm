# BOJ 15655 N과 M (6)

def combinations(start, result):
  if len(result) == m:
    print(" ".join(map(str, result)))
  for i in range(start, n):
    result.append(array[i])
    combinations(i + 1, result)
    result.pop()

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
combinations(0, [])
