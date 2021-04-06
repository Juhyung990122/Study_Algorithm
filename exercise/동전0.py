import sys

n,k = map(int,sys.stdin.readline().split())
price = list()
for _ in range(n):
    price.append(int(sys.stdin.readline().rstrip()))

price.sort(reverse=True)
answer = 0
for p in price:
    if k == 0 :
        break
    answer += k // p
    k = k % p

print(answer) 