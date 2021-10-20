n,m = map(int,input().split())
trees = list(map(int,input().split()))

start, end = 1, max(trees)

while start <= end : 
    mid = (start + end) // 2
    total = 0
    for i in trees:
        tree = i - mid
        if tree > 0:
            total += tree

    if total >= m:
        start = mid + 1

    else:
        end = mid - 1

print(end)
