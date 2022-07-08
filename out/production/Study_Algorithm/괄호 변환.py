def divide(w):
    open = 0
    close = 0

    for i in range(len(w)):
        if w[i] == "(":
            open += 1
        else:
            close += 1

        if open == close:
            return w[:i+1] , w[i+1:]


def correct(u):
    stack = []
    for pick in u:
        if pick == "(":
            stack.append(pick)
        else:
            if not stack:
                return False
            stack.pop()
    return True
            


def solution(p):
    answer = ''
    if p == "":
        return ""
    
    u,v = divide(p)

    if correct(u):
        return u + solution(v)
    
    else:
        string = "(" + solution(v) + ")"
        u = u[1:-1]
        convert_u = ""
        for i in u:
            if i == "(":
                convert_u += ")"
            else:
                convert_u += "("
        answer = string + convert_u

    return answer

print(solution("(()())()"))