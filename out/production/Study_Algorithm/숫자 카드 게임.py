n,m = map(int,input().split())

cards = list()
for i in range(n):
    cards.append(list(map(int,input().split())))

result = []
for i in cards:
    minValue = 10001
    for j in i:
        if minValue > j:
            minValue = j
    result.append(minValue)
print(max((result)))