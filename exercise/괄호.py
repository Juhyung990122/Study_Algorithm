import sys

t = int(sys.stdin.readline())
input_list = list(sys.stdin.readline().rstrip() for _ in range(t))

for check_list in input_list:
    check_list = list(check_list)
    queue = list()

    vps = True
    for check in check_list:
        if check == '(':
            queue .append(check)
        else:
            if queue and queue[0] == '(':
                queue.pop(0)
            else:
                queue.append(check)
    
    if stack:
        vps = False

    if vps == True:
        print("YES")
    else:
        print("NO")
    