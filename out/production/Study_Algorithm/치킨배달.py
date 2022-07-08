

import itertools


n,m = map(int,input().split())
graph = list()
chicken = list()
home = list()
for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))
        if graph[i][j] == 2:
            chicken.append((i,j))

chicken_list = list(itertools.combinations(chicken,m))
sum = 9999999
for comb in chicken_list:
    sum_distance = 0
    for c in range(len(comb)):
        for h in home:
            sum_distance += min(list(abs(comb[c][0]-h[0])+abs(comb[c][1]-h[1])))

        if sum_distance < sum:
            sum = sum_distance
print(sum)


