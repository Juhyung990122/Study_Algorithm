import sys
from collections import deque

k = int(sys.stdin.readline())
call = list()
for _ in range(k):
    input_num = int(sys.stdin.readline().rstrip())
    call.append(input_num)

queue = deque()

for i in call:
    if i == 0:
        queue.pop()
    else:
        queue.append(i)

print(sum(queue))

