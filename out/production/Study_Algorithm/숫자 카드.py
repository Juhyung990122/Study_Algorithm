n = int(input())
have = sorted(list(map(int,input().split())))
m = int(input())
card = list(map(int,input().split()))


def binary(num):
    start = 0
    end = n - 1
    while start <= end : 
        mid = (start + end)// 2
        if num == have[mid]:
            return 1
        elif num > have[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in card:
    print(binary(i),end = ' ')
