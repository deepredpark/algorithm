n = int(input())
non_charge_list = [4, 7]
count = n // 5

if n in non_charge_list:
    count = -1
else:
    if n % 5 == 0:
        pass
    elif (n % 5 == 1) or (n % 5 == 3):
        count += 1
    else:
        count += 2

print(count)
