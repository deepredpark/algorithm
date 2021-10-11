import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
  command = sys.stdin.readline().rstrip()

  if command[:3] == 'pus':
    stack.append(command.split()[1])
  elif command == 'pop':
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif command == 'size':
    print(len(stack))
  elif command == 'empty':
    if not stack:
      print(1)
    else:
      print(0)
  else:
    if stack:
      print(stack[-1])
    else:
      print(-1)
