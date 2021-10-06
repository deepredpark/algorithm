string = input().lower()
alpha = list(set(string))

counts = []
counts_list = []
for i in range(len(alpha)):
    counts.append([i, string.count(alpha[i])])
    counts_list.append(string.count(alpha[i]))

counts.sort(key=lambda x: x[1])
if counts_list.count(max(counts_list)) > 1:
    print("?")
else:
    x, max_value = counts[-1]
    print(alpha[x].upper())
