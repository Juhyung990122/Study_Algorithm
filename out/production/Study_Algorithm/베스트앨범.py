def solution(genres, plays):
    answer = []
    play = dict()
    for i in set(genres):
        play[i] = [0]
    for i in range(len(plays)):
        play[genres[i]].append((i,plays[i]))
        play[genres[i]][0] += plays[i]
    play = sorted(play.items(),reverse=True,key = lambda x : x[1][0])
    for key,value in play:
        k = sorted(value[1:],reverse=True,key=lambda x : x[1])
        if len(k) == 1:
            answer.append(k[0][0])
            continue
        answer.append(k[0][0])
        answer.append(k[1][0])
    return answer
print(solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))