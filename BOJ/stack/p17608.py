import sys

n = int(sys.stdin.readline())

sticks = []
for _ in range(n):
  sticks.append(int(sys.stdin.readline()))

start_stick = sticks.pop()
count = 1
while sticks:
  stick = sticks.pop()
  if start_stick < stick:
    start_stick = stick
    count += 1
  
print(count)
