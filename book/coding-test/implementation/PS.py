# Review 2
# Implementation
# Matrix
matrix = []
for i in range(5):
  matrix.append([])
  for j in range(5):
    matrix[i].append(j)
  
print(matrix)

# page110 상하좌우
n = int(input())
command = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
command_dic = {'U':0, 'D':1, 'L':2, 'R':3}

x, y = 1, 1
for i in command:
  nx = x + dx[command_dic[i]]
  ny = y + dy[command_dic[i]]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny
  
print(x, y)

# page113 시각 4min 30sec
n = int(input())

count = 0
for hr in range(n + 1):
  for min in range(60):
    for sec in range(60):
      time = str(hr) + str(min) + str(sec)
      if '3' in time:
        count += 1
print(count)

# page115 왕실의 나이트 8min 30sec

y, x = list(input())
# other solution
# y = int(ord(y)) - int(ord('a')) + 1
alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
x = int(x)
y = alpha[y]

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1 ,1, -2, 2, -2, 2]

count = 0
for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > 8 or ny > 8:
    continue
  count += 1

print(count)

# page118 게임개발 35 min

n, m = map(int, input().split())
# view 0 북 1 동 2 남 3 서
x, y, view = map(int, input().split())
matrix = []
# 0은 육지, 1은 바다
for _ in range(n):
  matrix.append(list(map(int, input().split())))

# 북 -> 서 -> 남 -> 동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
matrix[x][y] = 2
cycle = 0
while True:
  if cycle == 4:
    nx = x - dx[view]
    ny = y - dy[view]
    if nx < 0 or ny < 0 or nx >= n or ny >= m or matrix[nx][ny] == 1 or matrix[nx][ny] == 2:
      break
    matrix[ny][ny] = 2
    x, y = nx, ny

  if view == 0:
    view = 3
  else:
    view -= 1
  nx = x + dx[view]
  ny = y + dy[view]
  if nx < 0 or ny < 0 or nx >= n or ny >= m or matrix[nx][ny] == 1 or matrix[nx][ny] == 2:
    cycle += 1
    continue
  matrix[nx][ny] = 2
  x, y = nx, ny
  cycle = 0

result = 0
for i in range(n):
  for j in range(m):
    if matrix[i][j] == 2:
      result += 1
print(result)
