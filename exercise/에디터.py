from sys import stdin
#시간제한이 빡세면 stdin 쓸것. 

left_stack= list(stdin.readline().strip())
right_stack=list()
m = int(input())


for _ in range(m):
    #한줄씩 쭉 입력받을 수 있음!
    order = stdin.readline()
    if order[0] == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
        else:
            pass
            
    elif order[0] == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
        else:
            pass
   
    elif order[0] == "B":
        if left_stack:
            left_stack.pop()
        else:
            pass
    else:
        left_stack.append(order[2])
        
#리스트를 문자열로 출력
#reversed하면 리스트 반환하긴하지만 can only concatenate list (not "list_reverseiterator") to list 이거 뜨니까 list 로 변환해줄것
print(''.join(left_stack+list(reversed(right_stack))))
        
        