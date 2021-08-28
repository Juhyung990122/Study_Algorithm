import sys
t = int(sys.stdin.readline())
num_list = list()
for _ in range(t):
    n = int(sys.stdin.readline())
    snum = list(map(int,sys.stdin.readline().split()))
    num_list.append(snum)

for i in range(t):
    student = [-1] + [0] * len(num_list[i])
    group = 0
    for j in range(1,len(num_list[i])+1):
        if student[num_list[i][j-1]] == 0:
            group += 1
            while student[num_list[i][j-1]] == 0:
                student[num_list[i][j-1]] = group
                j = num_list[i][j-1]

            while student[num_list[i][j-1]] == group:
                student[num_list[i][j-1]] = -1
                j = num_list[i][j-1]
    count = 0
    for answer in student:        
        if answer != -1:
            count += 1
    print(count)

