#Greedy 1 큰수의 법칙

n,m,k = map(int,input().split())
numlist = list(map(int,input().split()))

numlist.sort()
first = numlist[n-1]
second = numlist[n-2]

answer = 0

while True:
    for i in range(k):
        if m == 0 :
            break
        answer += first
        m -= 1
    if m == 0:
        break
    answer += second
    m -= 1

print(answer)

# 개선안
n,m,k = map(int,input().split())
numlist = list(map(int,input().split()))

numlist.sort()

first = numlist[n-1]
second = numlist[n-2]

answer = 0
count = m//(k+1) * k + m % (k+1)

answer = count * first
answer +=  (m - count) * second

print(answer)


