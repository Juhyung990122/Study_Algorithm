#떡볶이 떡 만들기
n,m = map(int,input().split(' '))
dduck= list(map(int,input().split()))
start = 0
end = max(dduck)
answer = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in dduck:
        if i > mid:
            total += i - mid
    if total >=  m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)





