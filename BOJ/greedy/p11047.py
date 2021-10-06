n, coin_sum = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

count = 0
coins.reverse()
for coin in coins:
    if coin_sum < coin:
        continue
    count += coin_sum // coin
    coin_sum = coin_sum % coin

print(count)
