# Search
# 1. Sequential search

array = ['Haneul', 'Jonggu', 'Dongbin', 'Taeil', 'Sangwork']

for i in range(len(array)):
  if array[i] == 'Dongbin':
    break

print('index', i)

def sequential_search(array, target):
  for i in range(len(array)):
    if array[i] == target:
      break
  return i

print(sequential_search(array, 'Taeil'))

# 2. Binary search
array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def binary_search(array, start, end, target):
  if start > end:
    return None
  mid = (start + end) // 2
  
  if array[mid] > target:
    return binary_search(array, start, mid - 1, target)
  elif array[mid] < target:
    return binary_search(array, mid + 1, end, target)
  else:
    return mid
  
print(binary_search(array, 0, len(array)-1, 4))  

# solution 2

array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def binary_search(array, start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1  
  return None

print(binary_search(array, 0, len(array)-1, 3))
