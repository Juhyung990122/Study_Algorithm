import sys
n = int(sys.stdin.readline())
numbers = [0]+list(int(sys.stdin.readline().rstrip()) for _ in range(n))
cycle = [0] * (n+1)
answer = list()

for i in range(1,n+1):
    if cycle[i] == 0:
        cycle_num = i
        while cycle[i] == 0:
            cycle[i] = cycle_num
            i = numbers[i]
            #쭉 들어가는거 번호매기고
            print(cycle)
        while cycle[i] == cycle_num:
            answer.append(i)
            cycle[i] = -1
            #사이클이 성립할때는 이전걸로 돌아감. 안되면 while문 조건안맞아서 정지
            i = numbers[i]

answer.sort()
print(cycle.count(-1))
for j in answer:
    print(j)