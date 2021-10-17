# page 220 - 54 min
# My solution
import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().rstrip().split()))

DP = [0] * n
DP[0] = array[0]
DP[1] = array[1]
DP[2] = array[2] + DP[0]

for i in range(3, n):
  DP[i] = max(array[i] + DP[i - 2], array[i] + DP[i - 3])

print(DP[n - 1])

# solution - Dongbin Na
# a[i] = max(a[i-1], a[i-2] + k[i])
import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
