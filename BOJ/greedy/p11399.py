n = int(input())
time_list = list(map(int, input().split()))
time_list.sort()

time_sum = time_list[0]
result = time_sum
for i in range(1, n):
    time_sum += time_list[i]
    result += time_sum

print(result)
