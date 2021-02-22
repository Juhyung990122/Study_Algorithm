n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
answer  = 0
a = sorted(a)

for i in range(n):
    answer += max(b) * a[i]
    b.remove(max(b))
print(answer)