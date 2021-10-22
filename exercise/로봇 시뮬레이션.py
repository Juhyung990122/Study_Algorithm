n = int(input())
student_list = dict()
graph = [[0]* n for _ in range(n) ]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

for _ in range(n**2):
    input_d = list(map(int,input().split()))
    student = input_d[0]
    like_list = input_d[1:]
    student_list[student] = like_list

for s in student_list:
    max_like = -1
    max_empty = -1
    fix_y = 0
    fix_x = 0 
    for y in range(n):
        for x in range(n):
            if graph[y][x] == 0:
                like_count = 0
                empty_count = 0 
                for k in range(4):
                    l_y = y + dy[k]
                    l_x = x + dx[k]
                    if l_y < 0 or n <= l_y or l_x < 0 or n <= l_x:
                        continue                     
                    if graph[l_y][l_x] == 0:
                        empty_count += 1
                    if graph[l_y][l_x] in student_list[s]:
                            like_count += 1

                if max_like < like_count or (max_like == like_count and max_empty < empty_count):
                    fix_y = y
                    fix_x = x
                    max_like = like_count
                    max_empty = empty_count
    graph[fix_y][fix_x] = s

answer = 0 
score = {0:0, 1:1, 2:10, 3:100, 4:1000}
for i in range(n):
    for j in range(n):
        now = graph[i][j]
        like_c = 0
        for k in range(4):
            move_y = i + dy[k]
            move_x = j + dx[k]
            if move_y < 0 or n <= move_y or move_x < 0 or n <= move_x:
                continue
            if graph[move_y][move_x] in student_list[now]:
                like_c += 1
        answer += score[like_c]

print(answer)
                    
