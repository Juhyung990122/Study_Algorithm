#부품찾기
def Binary(start,end,target):
    if start <= end:
        mid = (start + end) // 2
        if bupum_list[mid] == target:
            return mid
        elif bupum_list[mid] < target:
            return Binary(mid+1,end,target)
        else:
            return Binary(start,mid-1,target)
    return None


def Binary2(start,end,target):
    while start<=end:
        mid = (start + end) // 2
        if bupum_list[mid] == target:
            return mid
        elif bupum_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
bupum_list = list(map(int,input().split(' ')))
m = int(input())
req_list = list(map(int,input().split(' ')))


bupum_list=sorted(bupum_list)
req_list = sorted(req_list)

for i in req_list:
    result = Binary(0,n-1,i)
    if result != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')

#계수정렬풀이

