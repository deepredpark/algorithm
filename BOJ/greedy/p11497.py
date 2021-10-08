import sys

def level_print(woods, n):
  woods.sort()
  woods_weight = [0] * n
  
  left = 0
  right = -1
  for i in range(n):
    if i % 2 == 0:
      woods_weight[left] = woods[i]
      left += 1
    else:
      woods_weight[right] = woods[i]
      right -= 1
  
  level = woods_weight[-1] - woods_weight[0]
  for i in range(n-1):
    if level < abs(woods_weight[i] - woods_weight[i+1]):
      level = abs(woods_weight[i] - woods_weight[i+1])
  
  return level

test_number = int(sys.stdin.readline())
for i in range(test_number):
  n = int(sys.stdin.readline())
  woods = list(map(int, sys.stdin.readline().split()))
  print(level_print(woods, n))
