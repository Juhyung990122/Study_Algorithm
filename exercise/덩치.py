n = int(input())
people = []
answer = [1 for _ in range(n)]

for _ in range(n):
    people.append(list(map(int,input().split())))

for i in range(len(people)):
    target = people[i]
    for j in range(len(people)):
        if i == j :
            continue
        compare = people[j]
        if target[0] < compare[0] and target[1] < compare[1]:
            answer[i] += 1

print(" ".join(str(a) for a in answer))


