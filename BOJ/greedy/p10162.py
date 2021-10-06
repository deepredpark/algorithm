T = int(input())
times = [300, 60, 10]

count = []
for time in times:
    if time > T:
        count.append(0)
    else:
        count.append(T // time)
        T %= time

if T == 0:
    print(count[0], count[1], count[2])
else:
    print(-1)
