# BOJ 2580 스도쿠
import sys
input = sys.stdin.readline

def check(point):
  x, y = point
  impossible = []
  for i in range(9):
    impossible.append(graph[x][i])
  for i in range(9):
    impossible.append(graph[i][y])
  miniX = (x // 3) * 3
  miniY = (y // 3) * 3
  for i in range(3):
    for j in range(3):
      impossible.append(graph[miniX + i][miniY + j])
  possible = set([x for x in range(1, 10)]) - set(impossible)
  return list(possible)

def sudoku(index):
  global solve
  if solve == True:
    return
  if index == len(zeroIndex):
    solve = True
    for row in range(9):
      for col in range(9):
        print(graph[row][col], end=" ")
      print()
    return
  x, y = zeroIndex[index]
  for i in check((x, y)):
    graph[x][y] = i
    sudoku(index + 1)
    graph[x][y] = 0

graph = []
for _ in range(9):
  graph.append(list(map(int, input().split())))
zeroIndex = []
for x in range(9):
  for y in range(9):
    if graph[x][y] == 0:
      zeroIndex.append((x, y))
solve = False
sudoku(0)
