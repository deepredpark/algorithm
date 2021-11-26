# BOJ 15663 N과 M (9)

def dfs(result):
  global result2
  if len(result) == m:
    result2.append([array[x] for x in result])
    return
  for i in range(n):
    if i in result:
      continue
    result.append(i)
    dfs(result)
    result.pop()

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
result2 = []
dfs([])

result2.sort()
print(" ".join(map(str, result2[0])))
for i in range(1, len(result2)):
  if result2[i - 1] != result2[i]:
    print(" ".join(map(str, result2[i])))
