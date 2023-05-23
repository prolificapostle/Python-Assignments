from collections import deque

que1 = deque([])
que1.append(1)
que1.append(2)
que1.append(3)
que1.append(4)
print(que1)
que1.popleft()
que1.append(1)
que1.popright()
print(que1)
print(que1.index(2))

