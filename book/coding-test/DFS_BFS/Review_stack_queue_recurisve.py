# Review
# stack
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

# 파이썬에서 stack을 사용할 때는 별도의 라이브러리가 필요없다(큐는 필요하다는 의미)
# 기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 작동한다.

# queue
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

queue.reverse()
print(queue)

# 리스트 자료형을 이용해 큐를 구현할 순 있지만 시간복잡도가 더 높아

# Recursive function

def recursive_function(i):
  # 재귀 함수에서 꼭 필요한 순환 조건
  if i == 100:
    return
  # 순환되는 곳 사이의 출력 함수는 바로 연속적으로 출력
  print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
  recursive_function(i+1)
  # 순환되는 곳 밖의 함수는 시스템 메모리 스택에 저장되어 위 함수가 종료되면 뒷 순서부터 실행
  print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

# Recursive function 2

def factorial(n):
  if n <= 1:
    return 1
  return n * factorial(n-1)

print(factorial(5))

# Recursive function 3
# 유클리드 호제법 최대공약수(GCD)
# A, B's GCD (A > B) = B, A % B's GCD (if A % B == 0, B is A,B's GCD)

def GCD(a, b):
  if a % b == 0:
    return b
  else :
    return GCD(b, a % b)

print(GCD(192, 162))

# 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있지만
# 반복문보다 유리한 경우도 있고, 불리한 경우도 있다.
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓이기 때문에
# 스택을 사용해야 할 때, 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.
