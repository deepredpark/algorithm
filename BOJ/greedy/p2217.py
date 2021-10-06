n = int(input())
ropes = []
for i in range(n):
    ropes.append(int(input()))

ropes.sort()
ropes.reverse()

max_weight = ropes[0]
for i in range(1, len(ropes)):
    result = ropes[i] * (i + 1)
    max_weight = max(max_weight, result)

print(max_weight)
