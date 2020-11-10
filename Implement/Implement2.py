#Implement2

n = int(input())
answer = 0


for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(s) or '3' in str(m) or '3' in str(h):
                answer += 1
            '''
            if '3' in str(h)+str(m)+str(s):
                answer += 1
            '''

print(answer)