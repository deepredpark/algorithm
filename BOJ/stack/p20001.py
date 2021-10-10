import sys

if sys.stdin.readline().rstrip() == '고무오리 디버깅 시작':
    stack = []
    while True:
        word = sys.stdin.readline().rstrip()
        if word == '문제':
            stack.append(1)
        elif word == '고무오리':
            if stack:
                stack.pop()
            else:
                stack.append(1)
                stack.append(1)
        else:
            break

if not stack:
    print('고무오리야 사랑해')
else:
    print('힝구')
