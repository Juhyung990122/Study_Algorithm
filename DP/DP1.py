#피보나치 최적화 - 메모이제이션 구현(탑다운)

d = [0]*100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]


#f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)
print(fibo(99))

#피보나치 최적화 - 보텀업

DP_Table=[0]*100

DP_Table[1] = 1
DP_Table[2] = 1
n = 99

for i in range(3,n+1):
    DP_Table[i] = DP_Table[i-1]+DP_Table[i-2]
#f(1) f(2) f(3) f(4) f(5) f(6)
print(DP_Table[n])
