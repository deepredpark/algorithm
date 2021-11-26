# BOJ 9663 N-Queen
# reference1 = https://www.youtube.com/watch?v=HRwFgtiqHH0 (backtracking idea)
# reference2 = https://ca.ramel.be/12 (colum_check idea)
# reference3 = https://velog.io/@supremo7/%EB%B0%B1%EC%A4%80-9663%EB%B2%88-N-Queen (recursiondepth error)
n = int(input())
col = [0] * (n + 1)
col_check = [False] * (n + 1)
count = 0

def promising(row):
  for i in range(1, row):
    if abs(col[row] - col[i]) == (row - i):
      return False
  return True

# backtracking은 stack 기반 dfs로 구현
def dfs(row):
  global count
  if row == n:
    count += 1
    return
  for i in range(1, n + 1):
    if col_check[i]:
      continue 
    col[row + 1] = i
    if promising(row + 1):
      col_check[i] = True
      dfs(row + 1)
      col_check[i] = False
  
dfs(0)
print(count)
