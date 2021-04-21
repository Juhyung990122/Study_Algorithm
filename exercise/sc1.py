def solution(skill, skill_trees):
    answer = 0
    skill_order = list(skill)
    for s in skill_trees:
        available = True
        s = list(s)
        visited = [0] * len(skill_order)
        for i in s:
            if i == skill_order[0]:
                visited[0] = 1
                continue
            if i in skill_order:
                if visited[skill_order.index(i)-1] == 1:
                    visited[skill_order.index(i)] = 1
                    available = True
                else:
                    available = False
                    break
        if available:
            answer += 1
    return answer

print(solution("CBD", ["C", "D", "CB", "BDA"]))