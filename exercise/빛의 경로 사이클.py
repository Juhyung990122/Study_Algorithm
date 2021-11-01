dy = [-1,1,0,0]
dx = [0,0,-1,1]

def solution(grid):
    answer = []
    n = len(grid)
    m = len(grid[0])
    visited = [[False]*4 for _ in range(m) for _ in range(n)]
    return answer
print(solution(["SL","LR"]))