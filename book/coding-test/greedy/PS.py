# Review 2
# greedy : 현재 상황에서 가장 좋은 것만 선택하는 방법
# note! : 햔재의 선택이 나중에 미칠 영향에 대해 고려하지 않는다.
# 특정한 문제를 만났을 때, 단순히 현재 상황에서
# 가장 좋아보이는 것만 선택해도 문제를 풀 수 있는지 파악 필요!

# page87 거스름돈 문제
# 화폐 종류(K), 시간복잡도 O(K)
n = int(input())
coins = [500, 100, 50, 10]

count = 0
for coin in coins:
  if n >= coin:
    count += n // coin
    n %= coin
print(count)

# page92 큰 수의 법칙 8 min
n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
result = (array[-1] * k + array[-2]) * (m // (k + 1)) + (array[-1] * (m % (k + 1)))
print(result)

# page96 숫자 카드 게임 4 min
n, m = map(int, input().split())

result = 0
for _ in range(n):
    row = list(map(int, input().split()))
    min_value = min(row)
    result = max(result, min_value)

print(result)

# page99 1이 될 때까지 15 min
n, k = map(int, input().split())
count = 0
while True:
    if n // k == 0:
        count += (n % k) - 1
        break
    if n % k == 0:
        n //= k
        count += 1
    else:
        count += n % k
        n -= n % k

print(count)

# page311 모험가 길드 1h
INF = int(1e9)

n = int(input())
array = list(map(int, input().split()))
array.sort()

count = 0
start = 0
while start < n:
    need = array[start]
    end = start + need - 1
    if end >= n:
        break
    while need < array[end]:
        new_need = array[end]
        end += array[end] - need
        need = new_need
        if end >= n:
            need = INF
            break
    if need == INF:
        break
    start = end + 1
    count += 1

print(count)

# solution
n = int(input())
array = list(map(int, input().split()))
array.sort()

# 총 그룹 수
result = 0
# 현재 그룹에 포함된 모함가의 수
count = 0

for i in array:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(count)

# page312 곱하기 혹은 더하기 15 min
array = list(map(int, input()))
result = array[0]
for i in range(1, len(array)):
    if result < 2 or array[i] < 2:
        result += array[i]
    else:
        result *= array[i]
print(result)


# page313 문자열 뒤집기 7min 30sec
array = input()

count = 0
start = array[0]
for i in array[1:]:
    if start != i:
        count += 1
        start = i

if count == 1:
    print(count)
else:
    print(count // 2)

# page314 만들 수 없는 금액 꼭 다시 풀기
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for x in coins:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x
print(target)
