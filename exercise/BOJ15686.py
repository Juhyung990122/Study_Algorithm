import sys, itertools

n,m = map(int,sys.stdin.readline().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

home = list()
chicken = list()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))
        else:
            continue

#될 수 있는 조합 전체 뽑고
chick_list = list(itertools.combinations(chicken, m))
answer = sys.maxsize
for i in range(len(chick_list)):
    now_comb  = chick_list[i]
    sum_distance = 0
    for j in range(len(home)):
        # 집마다 각 치킨집(조합안에 있는)과의 거리를 계산한 뒤 가장 작은 값을 뽑아서 더함.
        sum_distance += min(list(abs(now_comb[c][0]-home[j][0]) + abs(now_comb[c][1]-home[j][1]) for c in range(len(now_comb))))
    
    # 전체 도시의 치킨거리가 현재 치킨거리보다 가까우면 갱신!
    if sum_distance < answer: 
        answer = sum_distance

print(answer)



