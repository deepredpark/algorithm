# BOJ 1759 암호만들기
import sys
input = sys.stdin.readline
vowels = ['a', 'e', 'i', 'o', 'u']

def codeCase(start, count, result):
  if count > l - 2:
    return
  if len(result) == l and count > 0:
    print("".join(result))
    return
  for i in range(start, len(candidates)):
    if candidates[i] in vowels:
      count += 1
      result.append(candidates[i])
      codeCase(i + 1, count, result)
      count -= 1
      result.pop()
    else:
      result.append(candidates[i])
      codeCase(i + 1, count, result)
      result.pop()

l, c = map(int, input().split())
candidates = list(input().rstrip().split())
candidates.sort()
codeCase(0, 0, [])
