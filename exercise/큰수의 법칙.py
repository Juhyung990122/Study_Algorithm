n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data = sorted(data)

firstNum = data[-1]
secondNum = data[-2]

replay = (firstNum * k + secondNum) * (m // (k+1))
print(replay)
remain = firstNum * (m % (k+1))

answer = replay+remain
print(answer)