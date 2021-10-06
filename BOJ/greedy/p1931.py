#reference: https://daimhada.tistory.com/38

n = int(input())
confer_list = []

for i in range(n):
    confer_list.append(list(map(int, input().split())))

confer_list.sort(key=lambda x: x[0])
confer_list.sort(key=lambda x: x[1])

count = 0
start_time = 0

for time in confer_list:
    if time[0] >= start_time:
        start_time = time[1]
        count += 1

print(count)
