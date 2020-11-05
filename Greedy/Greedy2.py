#Greedy 2 숫자 카드 게임
n,m = map(int,input().split())
answer = 0

for i in range(n):
    card = list(map(int,input().split()))
    min_value = min(card)
    answer = max(answer, min_value)

print(answer)