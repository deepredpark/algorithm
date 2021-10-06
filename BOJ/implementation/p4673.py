def d(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    result = n + sum
    return result

nums = list(range(1, 10001))
self_nums = []
while nums:
    self_num = nums.pop(0)
    self_nums.append(self_num)
    while True:
        if d(self_num) in nums:
            nums.remove(d(self_num))
            self_num = d(self_num)
        else:
            break

for i in self_nums:
    print(i)
