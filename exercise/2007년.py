x,y = map(int,input().split())
m = [0] + [0] * 12
months = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

for i in range(1,12):
    m[i] = months[i-1] + m[i-1]
    
print(days[(m[x-1] + y) % 7])