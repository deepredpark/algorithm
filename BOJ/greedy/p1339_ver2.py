import sys
n = int(sys.stdin.readline())
words = []
for i in range(n):
  words.append(sys.stdin.readline().rstrip())

alpha_dic = {}
for i in set(''.join(words)):
  alpha_dic[i] = 0

for word in words:
  word = word[::-1]
  j = 0
  while j < len(word):
    alpha_dic[word[j]] += 1 * (10 ** j)
    j += 1

alpha_list = list(alpha_dic.items())
alpha_list.sort(reverse=True, key=lambda x: x[1])

sum = 0
for i in range(len(alpha_list)):
  sum += alpha_list[i][1] * (9 - i)
print(sum)
