import sys 

# 1~n번째 사람 나르는데 필요한 시간
def solution(n):
    if n < 3:
				# 총 인원이 1명 혹은 2명이면 가장 느린 사람 시간 
        return time_list[n-1]
    elif n == 3:
				# 총 인원이 3명이면 가장 빠른 사람이 한번 왕복
        return time_list[0]+time_list[1]+time_list[2]
    else:
        for i in range(len(time_list)):
						# 1~k-2번째 사람까지 나르고 + 가장 느린 두명 나르는 시간
						# 가장 빠른 사람이 두명을 따로따로 나르는 경우 or 가장 빠른 사람이 손전등 들고 갔다가 가장 느린 둘이 건너고, 두번째로 빠른 사람이 가장 빠른 사람을 데려오는 경우
            return solution(n-2) + min(time_list[n-1] + time_list[n-2] + 2 * time_list[0],time_list[0]+time_list[n-1]+time_list[1]*2)


n = int(sys.stdin.readline())
time_list = list()
for _ in range(n):
    time_list.append(int(sys.stdin.readline()))

time_list.sort()
print(solution(n))
