# Review
# Selective_sort()

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array) - 1):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]

print(array)

# Insertion_sort()

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  while i > 0:
    if array[i - 1] > array[i]:
      array[i -1], array[i] = array[i], array[i-1]
      i -= 1
    else:
      break

print(array)

#Dongbin Na solution

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j - 1] > array[j]:
      array[j -1], array[j] = array[j], array[j-1]
    else:
      break

print(array)

# Quick_sort()

array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  left = list(filter(lambda x: x < pivot, array[1:]))
  right = list(filter(lambda x: x >= pivot, array[1:]))
  
  return quick_sort(left) + [pivot] + quick_sort(right)
  
print(quick_sort(array))

# Dongbin Na solution 1

array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# Dongbin Na solution 2

array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end

  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
    
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# Count_sort()

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count_array = [0] * (max(array) + 1)

for i in range(len(array)):
  count_array[array[i]] += 1

result = []
for i in range(len(count_array)):
  for _ in range(count_array[i]):
    result.append(i)

print(result)
