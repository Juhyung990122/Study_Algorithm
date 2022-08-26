def solution(n, times):
    # 최소시간 최대시간 
    left,right = 1,max(times) * n
    answer = 0
    while left <= right:
        # 한 심사위원에게 주어진 시간
        mid = (left+right) // 2
        people = 0
        for i in times:
            # 각 심사위원마다, 몇명 심사할 수 있는지 
            people += mid // i
            # 다 심사할 수 있는 사람이 하나라도 있으면 break
            if people >= n :
                break
        
        # 모든 사람을 심사할 수 있다면
        if people >= n:
            # 시간을 줄여보고
            answer = mid
            right = mid - 1
        elif people < n :
            # 다 심사못해서 나온 케이스라면
            # 시간을 늘려본다.
            left = mid + 1
    return answer
print(solution(6,[7,10]))