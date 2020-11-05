#Greedy 3 1이 될 때
n,k = map(int,input().split())
answer = 0

while n != 1:
    if n % k == 0:
        n = n//k
        answer += 1
    else:
        n -= 1
        answer += 1

print(answer)

#개선안

n,k = map(int,input().split())
answer = 0
while True:
    target = (n//k) * k
    # 나누어떨어질때까지 1번 연산하는 횟수
    answer += n - target
    n = target
    if n < k :
        break
    #2번 연산하는 횟수
    n = n // k
    answer += 1

#1 아닌채로 나오게되면 1될때까지 1번연산 / 1이면 0되니까 상관없음.
answer += (n-1)
print(answer)
