def pick(p, board,picked):
    # 0이 아닐떄까지 y축 += 1
    for y in range(len(board)):
        if board[y][p] == 0:
            continue
        else:
            # list.append(숫자)
            # list[y][x] = 0
            picked.append(board[y][p])
            board[y][p] = 0
            break 
    return picked

def pang(picked,answer):
    if len(picked) > 1:
    # 맨윗숫자와 그 아래숫자 비교
        if picked[-1] == picked[-2]:
        # 같으면 pop() pop()
            picked.pop()
            picked.pop()
            answer += 2
        # 다르면 pass
        else:
            pass
    return answer
    

def solution(board, moves):
    answer  = 0

    picked = list()
    for i in moves:
        picked = pick(i-1,board,picked)
        answer = pang(picked,answer)
    return answer