import sys

n = int(sys.stdin.readline())
count_array = [0] * 10001
for _ in range(n):
  num = int(sys.stdin.readline())
  count_array[num] += 1

for i in range(len(count_array)):
  for _ in range(count_array[i]):
    print(i)
