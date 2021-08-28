def main():
    p,n,h = map(int,input().split())
    graph = dict()
    answer = [] 
    for i in range(1,p+1):
        graph[i] = list()
        
    for _ in range(n):
        pc_num, hour = map(int,input().split())
        graph[pc_num].append(hour)


    for pc in range(1,p+1):
        graph[pc].sort()
        for v in range(0,len(graph[pc])-1):
            if graph[pc][v] > h:
                graph[pc] = graph[pc][:v]
                break
    
    
    for pc in range(1,p+1):
        dp = [[]]
        dp.append([])
        reserv = graph[pc] #시간 담겨있는 리스트?
        if not graph[pc] :
            answer.append((pc,0))
            continue
        

        for i in range(len(reserv)):
            dp.append([])
            for j in range(h+1):
                dp[i].append(0)
                
        for t in range(reserv[0], h+1):
            dp[0][t] = reserv[0]

        for i in range(1,len(reserv)):
            for t in range(reserv[i]):
                dp[i][t] = dp[i-1][t]
            for t in range(reserv[i],h+1):
                dp[i][t] = max(dp[i-1][t],dp[i-1][t-reserv[i]]+reserv[i])

        answer.append((pc, dp[len(reserv)-1][h]))

    for i in answer:
        print(i[0], i[1] * 1000)

if __name__=="__main__":
    main()