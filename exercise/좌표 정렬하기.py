n = int(input())
num = list()

for _ in range(n):
    x,y = list(map(int,input().split()))
    num.append([x,y])

#비교할 아이템의 요소가 복수 개일 경우, 튜플로 그 순서를 내보내주면 된다.
num.sort(key = lambda x : (x[0],x[1]))

for i in num:
    print(i[0],i[1])
