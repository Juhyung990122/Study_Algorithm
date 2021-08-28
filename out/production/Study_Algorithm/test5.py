import sys

def permanent(stack,n):

    if len(stack) >= n:
        print(int(''.join(map(str,stack))))
    
    else:
        for i in range(1,n+1):

            if check[i] == 1:
                continue
            
            check[i] = 1
            stack.append(i)


            permanent(stack,n)


            check[i] = 0
            stack.pop()


while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    check = [0] * (n+1)
    stack =  list()
    permanent(stack,n)
    print()


