# BOJ 17298 오큰수
n = int(input())
array = list(enumerate(map(int, input().split())))
NGE = [-1] * n
stack = [array[0]]
for i in range(1, n):
  while stack[-1][1] < array[i][1]:
    NGE[stack[-1][0]] = array[i][1]
    stack.pop()
    if stack == []:
      stack.append(array[i])
  else:
    stack.append(array[i])

for i in NGE:
  print(i, end=' ')
