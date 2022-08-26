n,k = map(int,input().split())
answer = 0

while True:
    # 나눠지는 수 찾고
    target = (n // k) * k
    # 나눠지는 수 나올때까지 빼고 뺀걸 카운트에 더한다.
    answer += n - target
    # 나눠지는 수로 타겟설정 후
    n = target
    if n < k :
        # 더 나눌 수 없는 수가 되면 반복문을 나가서
        break
    # 나눠서 더한다
    answer += 1
    n //= k

#n이 1이 될때까지 더한다. 
answer += (n-1)
print(answer)
