import sys
n,k = map(int,sys.stdin.readline().split())
check = [False,False]+[True for _ in range(n+2)]
delete = 0

for i in range(2,n+1):
    if check[i]:
        for j in range(i, n+1, i):
            if check[j] == True:
                check[j] = False
                delete += 1
        
            if delete == k:
                print(j)
                break






