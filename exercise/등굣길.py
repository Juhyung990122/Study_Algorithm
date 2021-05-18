def solution(m, n, puddles):
    graph = [[0] * (m+1) for _ in range(n+1)]
    graph[1][1] = 1

    #오른쪽, 아래쪽 최단경로 갯수
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                continue
            if [j,i] in puddles:
                graph[i][j] = 0
            else:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
    return graph[n][m] % 1000000007

print(solution(3, 3, [[2, 3]]), 3)
print(solution(3, 3, [[1, 3]]), 5)
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) 
print(solution(4, 4, [[3, 2], [2, 4]]), 7)

