
import sys
from collections import deque


def check_left(start,dir,t_list):
    if start > 4 or t_list[start-1][2] == t_list[start][6]:
        return
    else:
        if t_list[start-1][2] != t_list[start][6]:
            check_left(start+1,-dir,t_list)
            t_list[start].rotate(dir)

def check_right(start,dir,t_list):
    if start > 4 or t_list[start-1][6] == t_list[start][2]:
        return
    else:
        if t_list[start-1][6] != t_list[start][2]:
            check_right(start-1,-dir,t_list)
            t_list[start].rotate(dir)


#dict 활용해보기

answer = 0


print(answer)