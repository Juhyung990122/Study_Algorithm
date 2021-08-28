import sys, itertools
n,k = map(int,sys.stdin.readline().split())
words = [0] * n
answer = 0

for i in range(n):
    input_data = sys.stdin.readline().rstrip()
    for x in input_data:
        #words 배열에 비트마스킹을 저장합니다. (아스키코드로 바꾼 x에서 알파벳 a 빼고 1 시프트하면 )
        words[i] |= (1 << (ord(x) - ord('a')))

if k < 5:
    print(0)
else:
    alpha = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
    need = ['a','c','t','i','n']
    for i in list(itertools.combinations(alpha, k-5)):
        each = 0
        res = 0
        for j in need:
            each |= (1 << (ord(j)-ord('a')))
        for j in i:
            each |= (1 << (ord(j)-ord('a')))
        
        for j in words:
            if each & j == j:
                res += 1
        
        if answer < res:
            answer = res
        
    print(answer)
