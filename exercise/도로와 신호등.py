n,l = map(int,input().split())
#지금 시간
now = 0
#총합 시간
answer = 0 

for _ in range(n):
    d,r,g = map(int,input().split())
    answer += d - now
    now = d 
    if answer % (r+g) <= r:
        #빨간불이라면?
        #빨간불 끝날때까지 대기하기
        answer += r-(answer%(r+g))
print(answer + l-now )