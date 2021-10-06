coins = [500, 100, 50, 10, 5, 1]
charge = 1000 - int(input())

count = 0
for coin in coins:
    if coin > charge:
        continue
    else:
        count += charge // coin
        charge %= coin

print(count)
