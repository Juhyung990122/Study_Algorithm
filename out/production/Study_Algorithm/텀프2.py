import sys
t = int(sys.stdin.readline())
num_list = list()
for _ in range(t):
    n = int(sys.stdin.readline())
    snum = list(map(int,sys.stdin.readline().split()))
    num_list.append(snum)

for i in range(t):
    student = [0] + num_list[i]
    answer = []
    visited = [0] * len(student)
    success = [0] * len(student)
    
    for j in range(1, len(student)):
        leader = j
        temp_team = []
        now = leader
        while True:
            if visited[student[now]] != leader:
                visited[student[now]] = leader
                temp_team.append(now)
                now = student[now]
            else:
                break
        if visited[leader] == leader:
            answer += temp_team
    print(len(student)-1-len((set(answer))))
                
