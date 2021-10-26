# 10818 최소, 최대
# no library
n = int(input())
array = list(map(int, input().split()))

min_index = 0
max_index = 0
for i in range(1, len(array)):
  if array[min_index] > array[i]:
    min_index = i
  if array[max_index] < array[i]:
    max_index = i

print(array[min_index], array[max_index])
