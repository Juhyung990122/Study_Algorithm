def solution(money):
    answer = [0]*9
    m_list = [50000,10000,5000,1000,500,100,50,10,1]
    for i in range(9):
        answer[i] = money // m_list[i]
        money = money % m_list[i]
    return answer
