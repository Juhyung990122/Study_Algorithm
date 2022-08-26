# 회의가 일찍 끝나는 대로 
n = int(input())
sc = []
for i in range(n):
    start,end = map(int,input().split())
    sc.append([start,end])

sc = sorted(sc , key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
#시작 == 끝 인경우를 위해서 재정렬
sc = sorted(sc , key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
answer = 0
now_end = 0

for start,end in sc:
    if start >= now_end:
        answer += 1
        now_end = end 

print(answer) 

