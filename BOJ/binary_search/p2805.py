n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 1
end = max(array)

while start <= end:
  mid = (start + end) // 2
  sum = 0
  for i in array:
    if i > mid:
      sum += i - mid
      if sum > m:
        break
        
  if sum < m:
    end = mid - 1
  else:
    start = mid + 1
  
print(end)
