
t = int(input())
for _ in range(t):
    queue = list()
    orderlist = list(input())

    for i in range(len(orderlist)):
        queue.append(orderlist[i])
    n = int(input())

    l = input()[1:-1]
    l = list(l.split(","))

    if len(orderlist) == 0:
        print("error")
        continue
    
    if len(l) == 0:
        print("error")
        continue

    r = 0
    for order in queue:
        flag = 0
        if order == "R":
            r += 1    
        
        elif order == "D":
            if len(l) == 0:
                flag = 1
                break
            else:
                if r % 2 == 0:
                    l.pop(0)
                else:
                    l.pop()
    
    if flag ==1:
        print("error")
        continue
    else:
        if r % 2 == 0:
            print(l)

        else:
            print(l[::-1])

