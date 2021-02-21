import collections

n = int(input())
m = list()
for i in range(0,n):
    m.append(list(input().split()))

q = collections.deque([])
for order in m:
    if order[0] == "push":
        q.append(int(order[1]))

    elif order[0] == "pop":
        if len(q) == 0:
            print("-1")
        else:
            print(q.popleft())
    
    elif order[0] == "size":
        print(len(q))
    
    elif order[0] == "empty":
        if len(q) == 0:
            print ("1")
        else:
            print ("0")
    
    elif order[0] == "front":
        if len(q) == 0:
            print ("-1")
        else:
            print (q[0])

    else:
        if len(q) == 0:
            print ("-1")
        else:
            print(q[-1])





