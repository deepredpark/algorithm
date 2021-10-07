import sys
n = int(sys.stdin.readline())
infoes = []
for i in range(n):
    infoes.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    x, y = infoes[i]
    count = 1
    for j in range(n):
        if i == j:
            continue
        nx, ny = infoes[j]
        if nx > x and ny > y:
            count += 1
    print(count, end=' ')
