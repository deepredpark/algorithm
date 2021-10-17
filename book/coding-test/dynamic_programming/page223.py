# page223 12min
# My solution

n = int(input())

start1 = 3 ** (n // 2)
start2 = 3 ** ((n - 1) // 2)

print((start1 + start2 - 1) % 796796)
