from collections import deque;
import sys

gears = dict()

for i in range(1, 5):
    gears[i] = deque((map(int, input())))
n = int(sys.stdin.readline())

def rotate(gear_num, rotate):
    gears[gear_num].rotate(rotate)

def change_dir(rotate):
    if(rotate == -1):
        rotate = 1
    else:
        rotate = -1
    return rotate
        
for i in range(n):
    gear_num, rotate_dir = map(int,sys.stdin.readline().split())
    rotate(gear_num, rotate_dir)
    print("asdf", gears)
    rotate_dir = change_dir(rotate_dir)

    next_gear_num = gear_num
    while(next_gear_num < 4):
        next_gear_num += 1
        if gears[gear_num][6] == gears[next_gear_num][2]:
            rotate(next_gear_num, rotate_dir)
            rotate_dir = change_dir(rotate_dir)
            gear_num = next_gear_num
            print(gears)