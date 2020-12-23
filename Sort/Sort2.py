n, k = map(int,input().split())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

answer = 0
a_list.sort()
b_list.sort(reverse=True)

for i in range(k):
    if a_list[i] < b_list[i]:
        a_list[i] = b_list[i]
        #바꾼다는 얘기가 있는데 이거 충족시킬거면 아래 코드 사용
        #a_list[i],b_list[i] = b_list[i],a_list[i]
    else:
        pass

for i in a_list:
    answer += i

print(answer)