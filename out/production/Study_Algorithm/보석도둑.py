import sys
n,k = map(int,sys.stdin.readline().split())
j_info = list(tuple(map(int,sys.stdin.readline().rstrip().split(' '))) for _ in range(n))
bag = list(int(sys.stdin.readline().rstrip()) for _ in range(k))
price_list = list()
answer = 0

bag.sort()
for j in j_info:
    price = j[1] / j[0]
    price_list.append((j[0],price,j[1]))
price_list.sort(key = lambda x : x[1], reverse= True)

for check in price_list:
    first = 0
    last = k -1
    while first <= last:
        mid = (first + last) // 2
        if bag[mid] == check[0]:
            answer += check[2]
            bag.pop(mid)
            break
        elif bag[mid] < check[0]:
            first = mid + 1
        else:
            last = mid -1

    if bag:
        answer += check[2]

        
    
    
    
