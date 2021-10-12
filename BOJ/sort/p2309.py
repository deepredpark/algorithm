import sys

array = []
total_sum = 0
for _ in range(9):
  num = int(sys.stdin.readline())
  array.append(num)
  total_sum += num

for i in range(len(array) - 1):
  for j in range(i + 1, len(array)):
    sum = total_sum - array[i] - array[j]
    if sum == 100:
      break

  if sum == 100:
    value1, value2 = array[i], array[j]
    array.remove(value1)
    array.remove(value2)
    break
  elif i == 8:
    array.pop()
    array.pop()

array.sort()
for i in array:
  print(i)
