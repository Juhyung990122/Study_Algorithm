def solution(sizes):
    answer = 0
    sizes = [sorted(size,reverse=True) for size in sizes]
    w = []
    h = []
    for i in sizes:
        w.append(i[0])
        h.append(i[1])

    answer = max(w) * max(h)
    return answer