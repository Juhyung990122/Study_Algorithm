def solution(ings, menu, sell):
    answer = 0
    g_list = dict()
    menu_list = dict()
    for i in ings:
        info = i.split(" ")
        g_list[info[0]] = int(info[1])
    for i in menu:
        info = i.split()
        m = info[0]
        g = list(info[1])
        p = info[2]
        menu_list[m] = [g,p]
    
    for i in sell:
        order = i.split(" ")
        make_price = 0
        need = menu_list[order[0]][0]
        sell_price = int(menu_list[order[0]][1])
        for n in need:
            make_price += g_list[n]
        answer += (sell_price - make_price) * int(order[1])
    return answer
print(solution(["r 10", "a 23", "t 124", "k 9"],["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"],["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))
print(solution(["x 25", "y 20", "z 1000"],["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"],["BBBB 3", "TTT 2"]))