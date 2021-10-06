codes = input()

one_list = codes.replace('0', ' ').split()
zero_list = codes.replace('1', ' ').split()

print(min(len(one_list), len(zero_list)))
