n = int(input())
num_list = sorted(list(map(int,input().split())))
m = int(input())
search = list(map(int,input().split()))

def binary(num):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if num == num_list[mid] :
            return 1
        elif num > num_list[mid] :
            start = mid + 1
        else: 
            end = mid - 1
    return 0

for i in search:
    print(binary(i))
   

