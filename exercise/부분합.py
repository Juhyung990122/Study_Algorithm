from operator import le
import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

left = 0
right = left + 1
answer = float('inf')
nums = sorted(nums)
sum_num = nums[left]

while left < len(nums) - 1 and right < len(nums):
    sum_num += nums[right]
    if sum_num >= s:
        answer = min(answer, right - left) + 1

        right = left + 1
        sum_num = nums[left]
        continue
    right += 1
if answer == float('inf'):
    answer = 0
print(answer)

# 1 2 3 4 5 5 7 8 9 10