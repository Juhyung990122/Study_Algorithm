def solution(routes):
    answer = 0
    # 진출시점이 가장 뒤에 있는애부터 돌아야하니까 정렬
    routes.sort(key=lambda x : x[1])
    # 최소값으로 초기화
    camera = -30000
    for route in routes:
        if camera <= route[0]:
            answer += 1
            camera = route[1]
    return answer
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))