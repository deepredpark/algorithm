n = int(input())

def cycle(n):
    first = n % 10
    n_mini = 0
    if n < 10:
        n_mini += n
    else:
        n_mini += (n // 10) + (n % 10)
    last = n_mini % 10
    result = str(first) + str(last)

    return int(result)

init_n = n
n = cycle(n)
count = 1
while n != init_n:
    n = cycle(n)
    count += 1

print(count)
