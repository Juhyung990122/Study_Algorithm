n = 10000
check = [0] * 10001
answer = 0

for i in range(1,n+1):
    num = sum(list(map(int,str(i))))
    if i+num < n+1:
        if check[i+num] == 0:
            check[i+num] = 1

for i in range(1,n+1):
    if check[i] == 0:
        print(i)
    