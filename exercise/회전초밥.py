from cmath import pi
import sys

n, d, k, c = map(int, sys.stdin.readline().split())
belt  = list()
for _ in range(n):
    belt.append(int(sys.stdin.readline()))

# 원형 + 연속
# 리스트 받아서 2개 붙이고

rotating_belt = belt * 2
# 슬라이딩 윈도우 해주고 
max_window = 0
answer = max_window
left = 0
right = k
while left < n:
    pick = rotating_belt[left:right]
    pick = set(pick)
    max_window = len(pick)
    if c not in pick:
        max_window += 1
    right += 1
    left += 1
    answer = max(max_window, answer)
print(answer)