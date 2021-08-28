# 풀이참고: https://jeongchul.tistory.com/670
# t_list 설정 아이디어 얻음.

import sys

n,m = map(int,sys.stdin.readline().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

t_list = [
    [(0,0), (0,1), (1,0), (1,1)], 
    [(0,0), (0,1), (0,2), (0,3)], 
    [(0,0), (1,0), (2,0), (3,0)], 
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], 
    [(0,0), (0,1), (0,2), (1,2)], 
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], 
    [(1,0), (1,1), (1,2), (0,1)], 
    [(0,0), (1,0), (2,0), (1,1)], 
    [(1,0), (0,1), (1,1), (2,1)], 
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

def find(x,y):
    global answer
    for i in range(19):
        # 모양당 결과값
        result = 0
        for j in range(4):
            # 한칸씩 그래프에 넣음
            try:
                next_x = x + t_list[i][j][0]
                next_y = y + t_list[i][j][1]
                result += graph[next_y][next_x]
            # 인덱스 넘어가면 넘기고
            except IndexError:
                continue
        answer = max(answer,result)

def solve():
    for i in range(n):
        for j in range(m):
            find(i,j)


answer = 0
solve()
print(answer)


                        
            
            

