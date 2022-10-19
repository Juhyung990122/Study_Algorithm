def solution(prices, discount):
    s_prices = sorted(prices)
    s_discounts = sorted(discount)

    answer = 0
    for i in range(0, len(s_discounts)):
        answer += s_prices[i] * (100 - s_discounts[i]) * 0.01

    while i < len(s_prices)-1:
        i += 1
        answer += s_prices[i]

    return answer

print(solution([1000,2000,3000,5000,4000], [10,20,30,40,10]))