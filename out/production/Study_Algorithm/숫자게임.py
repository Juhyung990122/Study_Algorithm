def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    while B:
        # 리스트 내 가장 작은 애들끼리 비교
        if A[0] < B[0]:
            # 이길 수 있으면
            answer += 1
            # A랑 짱뜰 B가 정해졌으니 A에서 빼준다.
            A.pop()
        # 비기거나 지는거면 짜피 답이 될 수 없으니 B에서 빼준다(다음걸로 넘어간다.)
        B.pop(0)

    return answer