def solution(A, B):
    A = sorted(A)
    B = sorted(B)
    win = 0
    while B:
        if len(A) == 0:
            return win
        
        if A[0] < B[0]:
            A.pop(0)
            win += 1
        B.pop(0)
    return win
print(solution([5, 1, 3, 7], [2, 2, 6, 8]))