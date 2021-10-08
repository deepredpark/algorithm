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

alpha_weigh = []
for i in alpha_dic.keys():
  alpha_weigh.append([i, alpha_dic[i]])

alpha_weigh.sort(reverse=True, key=lambda x: x[1])
alpha_dic = {}
for i in range(len(alpha_weigh)):
  weigh = 9 - i
  alpha_dic[alpha_weigh[i][0]] = str(weigh)

result = []
for word in words:
  mini_result = ''
  for i in word:
    mini_result += alpha_dic[i]
  result.append(int(mini_result))

sum = 0
for i in result:
  sum += i

print(sum)
