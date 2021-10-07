import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()

#1
sum = 0
for i in nums:
    sum += i
avg = round(sum / len(nums), 0)
print(int(avg))

#2
if len(nums) % 2 == 1:
    index = len(nums) // 2
    mid = nums[index]
else:
    index = len(nums) // 2
    mid = (nums[index-1] + nums[index]) // 2
print(mid)

#3
start = nums[0]
count = 0
max_count = 1
max_nums = []
for i in nums:
    if start == i:
        count += 1
        index = i
    else:
        start = i
        count = 1

    if count == max_count:
        max_nums.append(i)
    elif count > max_count:
        max_count = count
        max_nums = [i]
    else:
        pass

if len(max_nums) == 1:
    print(max_nums[0])
else:
    print(max_nums[1])

#4
print(nums[-1] - nums[0])
