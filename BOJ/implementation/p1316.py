def group_num(word):
    i = 0
    while True:
        count = word.count(word[i])
        if count == (len(word) - len(word.lstrip(word[i]))):
            word = word.lstrip(word[i])
        else:
            return False
        if not word:
            return True

n = int(input())

group_num_count = 0
for i in range(n):
    if group_num(input()):
        group_num_count += 1

print(group_num_count)
