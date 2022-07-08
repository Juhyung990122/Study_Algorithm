from collections import deque
n,k = map(int,input().split())
belt = deque(list(map(int,input().split())))
robot = deque([0]*n)

res = 0

while True:
    
    #한바퀴 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    # 로봇 들을 한번씩 옮기고
    if sum(robot):
        for i in range(n-2,-1,-1):
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
                robot[i+1] = 1
                robot[i] =0
                belt[i+1] -= 1
        robot[-1] = 0 
    #비어있으면 올리고
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    res += 1
    # 체크 
    if belt.count(0) >= k :
        break
    
print(res)
    

