import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
answer = list()

for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    doc = list(map(int,sys.stdin.readline().split()))
    for i in range(n):
        if i == m:
            doc[i] = [doc[i],1]
        else:
            doc[i] = [doc[i],0]
    
    queue = deque(doc)
    count = 0

    while queue:
        max_num = max(queue)
        now = queue.popleft()
        if now[0] == max_num[0]:
            count += 1
            if now[1] == 1:
                break
            continue
        else:
            queue.append(now)
        
    answer.append(count)
for i in answer:
    print(i)

        