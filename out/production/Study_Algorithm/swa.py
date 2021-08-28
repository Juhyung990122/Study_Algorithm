n = int(input())
start = list()
end = list()
for _ in range(n):
	time = input().split()
	start.append((time[0], int(time[0].split(':')[0]) * 60 + int(time[0].split(':')[1])))
	end.append((time[2], int(time[2].split(':')[0]) * 60 + int(time[2].split(':')[1])))
   
s = max(start, key=lambda x:x[1])
e = min(end, key=lambda x:x[1])

print(s[0], '~', e[0])
