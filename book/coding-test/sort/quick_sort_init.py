#retry this algorithm (recommend)

cards = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  #원소가 1개인 재귀함수 종료
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

quick_sort(cards, 0, len(cards)-1)
print(cards)
