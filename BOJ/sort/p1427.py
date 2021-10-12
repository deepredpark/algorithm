import sys

n = sys.stdin.readline().rstrip()
array = sorted(n, reverse=True)
print(''.join(array))
