#Implement1

size = int(input())
plan = list(input().split())

x,y = 1,1

for move in plan:
    if move == 'R':
        if y+1 > size:
            pass
        else:
            y += 1
    elif move == 'L':
        if y-1 <  1:
            pass
        else:
            y -= 1
    elif move == 'U':
        if x-1 < 1:
            pass
        else:
            x -= 1
    elif move == 'D':
        if x+1 > size:
            pass
        else:
            x += 1
print(x,y)
