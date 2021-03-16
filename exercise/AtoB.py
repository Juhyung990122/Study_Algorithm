import sys

a,b = map(int,sys.stdin.readline().split())
count = 1
while a != b:
    print(a,b)
    if (b % 10  != 1 and b % 2 != 0) or a > b:
        count = -1
        break
    #짝수
    else:
        if b % 2 == 0:
            b  = b // 2
        else:
            b  = b // 10
        count += 1
print(count)