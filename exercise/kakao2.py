def solution(places):
    answer = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for n in range(5):
        now_place = places[n]
        print(now_place)
        possible = 1
        for i in range(5):
            for j in range(5):
                if now_place[i][j] == 'P':
                    #앞뒤양옆
                    for move in range(8):
                        move_x = j + dx[move]
                        move_y = i + dy[move]
                        if 0 <= move_x < 5 and 0 <= move_y < 5 and now_place[move_y][move_x] == "P":
                            print('hit',i,j)
                            possible = 0
                            break
                    print('hey',i,j)
                    #대각선
                    c_x = [-1,1,-1,1]
                    c_y = [-1,1,1,-1]
                    for move in range(4):
                        move_x = j + c_x[move]
                        move_y = i + c_y[move]
                        if 0 <= move_x < 5 and 0 <= move_y < 5 and now_place[move_y][move_x] == "P":
                            if move_x == -1 and move_y == -1:
                                if now_place[move_y][move_x+1] != "X" and now_place[move_y+1][move_x] != "X":
                                    print('c1',now_place[move_y][move_x+1],now_place[move_y+1][move_x])
                                    possible = 0
                                    break
                            elif move_x == 1 and move_y == 1:
                                if now_place[move_y][move_x-1] != "X" and now_place[move_y-1][move_x] != "X":
                                    print('c2',now_place[move_y][move_x-1],now_place[move_y-1][move_x])
                                    possible = 0
                                    break
                            elif move_x == -1 and move_y == 1:
                                if now_place[move_y][move_x-1] != "X" and now_place[move_y+1][move_x] != "X":
                                    print('c3',now_place[move_y][move_x-1],now_place[move_y+1][move_x])
                                    possible = 0
                                    break
                            elif move_x == 1 and move_y == -1:
                                if now_place[move_y][move_x+1] != "X" and now_place[move_y-1][move_x] != "X":
                                    print('c4',now_place[move_y][move_x+1],now_place[move_y-1][move_x])
                                    possible = 0
                                    break
                                
                            possible = 0
                            break

        answer.append(possible)
         
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))