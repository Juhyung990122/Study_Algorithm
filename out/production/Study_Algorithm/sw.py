def main():
    n = int(input())
    road = list(map(int,input().split()))
    answer = []
    for i in [0,1,2]:
        visited = [0] * n
        now = i
        visited[now] = 1
        answer_r = 1
        while True:
            now += road[now]
            visited[now] += 1
            answer_r += 1
            if visited[now] > 1:
                answer.append(answer_r)
                break
    print(max(answer))
if __name__=="__main__":
    main()