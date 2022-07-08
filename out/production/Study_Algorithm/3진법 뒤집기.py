def solution(n):
    t = ''
    while n > 0:
        n,mod = divmod(n,3)
        t += str(mod)

    return int(t,3)

print(solution(45))