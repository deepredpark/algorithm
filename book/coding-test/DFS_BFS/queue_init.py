#page129
from collections import deque

#큐(Queue) 구현을 위해 python에서는 deque 개체를 생성하는 것이 거의 관행.
#리스트로 큐를 구현하는 것보다 시간복잡도가 낮다.
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
