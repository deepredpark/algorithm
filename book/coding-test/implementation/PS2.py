# Review 2
# Implementation
# page321 럭키 스트레이트 7min
n = input()
index = len(n) // 2
n1 = n[:index]
n2 = n[index:]
sum1 = 0
sum2 = 0
for i in range(len(n1)):
  sum1 += int(n1[i])
  sum2 += int(n2[i])

if sum1 == sum2:
  print('LUCKY')
else:
  print('READY')

# page322 문자열 재정렬3min
array = input()
alpha = []
sum = 0

for i in array:
  if i.isalpha():
    alpha.append(i)
  else:
    sum += int(i)

alpha.sort()
print(''.join(alpha) + str(sum))

# page323 문자열 압축 다시 풀것!

def solutions(s):
  answer = len(s)
  for step in range(1, len(s) // 2 + 1):
    compressed = ''
    prev = s[0:step]
    count = 1
    for j in range(step, len(s), step):
      print('len =', len(s), 'j + step =', j + step)
      if prev == s[j:j + step]:
        count += 1
      else:
        compressed += str(count) + prev if count >= 2 else prev
        prev = s[j:j + step]
        count = 1
    compressed += str(count) + prev if count >= 2 else prev
    print(compressed)
    answer = min(answer, len(compressed))
  return answer

s = input()
print(solutions(s))
