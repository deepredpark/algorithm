import sys
n = int(sys.stdin.readline())
cards = []
for i in range(n):
  cards.append(int(sys.stdin.readline()))

cards.sort()
sum = 0
for i in range(n-1):
  cards[i], cards[i+1] = 0, cards[i] + cards[i+1]
  sum += cards[i+1]
  for j in range(i+1, len(cards)-1):
    if cards[j] <= cards[j+1]:
      break
    else:
      cards[j], cards[j+1] = cards[j+1], cards[j]

print(sum)
